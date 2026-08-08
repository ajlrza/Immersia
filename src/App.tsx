import { useState } from 'react';
import { startRender, resetCanvas} from './services/render.js';
import './App.css';

const ICON_STROKE = 1.75;

function Icon({ path, size = 16 }) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth={ICON_STROKE}
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d={path} />
    </svg>
  );
}

const ICON_PATHS = {
  bolt: 'M13 10V3L4 14h7v7l9-11h-7z',
  refresh: 'M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15',
  cursor: 'M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5',
  edit: 'M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z',
  scroll: 'M7 16V4m0 0L3 8m4-4l4 4m6 0v12m0 0l4-4m-4 4l-4-4',
  play: 'M5 3l14 9-14 9V3z',
  plus: 'M12 4v16m8-8H4',
  cpu: 'M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z',
  monitor: 'M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z',
  home: 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6',
  world: 'M12 3l8 4.5v9L12 21l-8-4.5v-9L12 3z',
};

const ACTIONS = [
  {
    id: 'click',
    label: 'Click Element',
    shortcut: '⌘C',
    color: 'violet',
    icon: ICON_PATHS.cursor,
    fields: [
      { key: 'x', label: 'X', placeholder: '0' },
      { key: 'y', label: 'Y', placeholder: '0' },
    ],
  },
  {
    id: 'type',
    label: 'Type Text',
    shortcut: '⌘T',
    color: 'violet',
    icon: ICON_PATHS.edit,
    fields: [{ key: 'text', label: null, placeholder: 'Enter text to type…', full: true }],
  },
  {
    id: 'scroll',
    label: 'Scroll Page',
    shortcut: '⌘S',
    color: 'teal',
    icon: ICON_PATHS.scroll,
    fields: [
      { key: 'dx', label: 'ΔX', placeholder: '0' },
      { key: 'dy', label: 'ΔY', placeholder: '300' },
    ],
  },
];

const OBSERVATIONS = [
  { id: 'dom', label: 'View DOM Tree', dot: 'emerald' },
  { id: 'a11y', label: 'View A11y Tree', dot: 'default' },
  { id: 'bbox', label: 'Bounding Boxes', dot: 'indigo' },
];

const MAX_STEP = 4;

function App() {
  const [selectedAction, setSelectedAction] = useState('click');
  const [activeObs, setActiveObs] = useState({ dom: true, a11y: false, bbox: false });
  const [step, setStep] = useState(0);

  const handleReset = () => {
      resetCanvas();
      setStep(0);
    };

  const handleExecute = () => setStep((s) => Math.min(s + 1, MAX_STEP));

  const toggleObs = (id) => setActiveObs((prev) => ({ ...prev, [id]: !prev[id] }));
  const isRunning = step > 0;

  return (
    <div className="app-shell">
      {/* ── Header ── */}
      <header className="header-bar">
        <div className="brand-group">
          <div className="brand-mark">
            <Icon path={ICON_PATHS.world} size={17} />
          </div>
          <div className="brand-text">
            <span className="brand-title">
              Immersia
              <span className="brand-version">v0.1</span>
            </span>
            <span className="brand-sub">Web World Model</span>
          </div>
        </div>

        <div className="header-actions">
          <button onClick={startRender} className="btn-primary">
            <Icon path={ICON_PATHS.bolt} size={14} />
            Initialize
          </button>
          <button onClick={handleReset} className="btn-secondary">
            <Icon path={ICON_PATHS.refresh} size={14} />
            Reset
          </button>
        </div>

        <div className="header-status">
          <div className="status-counter">
            <span className="label">Step</span>
            <span className="val">{step}</span>
            <span className="sep">/</span>
            <span className="max">∞</span>
          </div>
          <div className={`status-pill ${isRunning ? 'is-running' : 'is-idle'}`}>
            <span className="ping-wrapper">
              {isRunning && <span className="ping-anim" />}
              <span className="ping-dot" />
            </span>
            <span>{isRunning ? 'Predicting' : 'Awaiting Action'}</span>
          </div>
        </div>
      </header>

      {/* ── Main layout ── */}
      <div className="main-layout">
        {/* Sidebar: Action Space */}
        <aside className="sidebar">
          <div className="section-header">
            <span className="eyebrow">Agent controls</span>
            <p className="section-title">Action Space</p>
          </div>

          <div className="action-list">
            {ACTIONS.map((action) => (
              <div
                key={action.id}
                className={`action-card ${selectedAction === action.id ? 'is-active' : ''}`}
              >
                <button className="action-btn" onClick={() => setSelectedAction(action.id)}>
                  <div className={`icon-box ${action.color}`}>
                    <Icon path={action.icon} size={15} />
                  </div>
                  <span>{action.label}</span>
                  <kbd className="shortcut-key">{action.shortcut}</kbd>
                </button>
                <div className={`input-container ${action.fields.length > 1 ? 'input-row' : ''}`}>
                  {action.fields.map((field) =>
                    field.full ? (
                      <input key={field.key} type="text" placeholder={field.placeholder} className="form-input" />
                    ) : (
                      <div key={field.key} className="input-group">
                        <label className="input-label">{field.label}</label>
                        <input type="number" placeholder={field.placeholder} className="form-input" />
                      </div>
                    )
                  )}
                </div>
              </div>
            ))}

            <button className="btn-execute" onClick={handleExecute}>
              <Icon path={ICON_PATHS.play} size={13} />
              Execute Action
            </button>
          </div>

          <div className="divider" />

          <div className="observations">
            <span className="eyebrow">World state readout</span>
            <div className="obs-list" style={{ marginTop: 12 }}>
              {OBSERVATIONS.map((obs) => (
                <button
                  key={obs.id}
                  className={`obs-btn ${activeObs[obs.id] ? 'is-active' : ''}`}
                  onClick={() => toggleObs(obs.id)}
                >
                  <div className="dot-box">
                    <div className={`dot ${obs.dot}`} />
                  </div>
                  <span>{obs.label}</span>
                </button>
              ))}
            </div>
          </div>
        </aside>

        {/* Center: Canvas */}
        <main className="canvas-area">
          <div className="canvas-wrapper">
            <div className="canvas-chrome">
              <div className="chrome-dots">
                <span />
                <span />
                <span />
              </div>
              <div className="chrome-address">
                immersia://world · <b>predicted state s{step}</b>
              </div>
            </div>

            <div className="sim-page">
              {/* Navbar */}
              <div className="sim-navbar">
                <div className="sim-nav-links">
                  <div className="sim-box dark" style={{ width: 96, height: 16 }} />
                  <div style={{ display: 'flex', gap: 20 }}>
                    <div className="sim-box" style={{ width: 48, height: 12 }} />
                    <div className="sim-box" style={{ width: 64, height: 12 }} />
                    <div className="sim-box" style={{ width: 40, height: 12 }} />
                    <div className="sim-box" style={{ width: 56, height: 12 }} />
                  </div>
                </div>
                <div style={{ display: 'flex', gap: 12, alignItems: 'center' }}>
                  <div className="sim-box" style={{ width: 80, height: 12 }} />
                  <div className="sim-box primary" style={{ width: 64, height: 28, borderRadius: 6 }} />
                </div>
              </div>

              {/* Hero */}
              <div className="sim-hero">
                <div
                  className="sim-box"
                  style={{ width: 64, height: 20, borderRadius: 20, marginBottom: 20, background: 'var(--predicted-soft)' }}
                />
                <div className="sim-box dark" style={{ width: '66%', height: 28, marginBottom: 12 }} />
                <div className="sim-box dark" style={{ width: '50%', height: 28, marginBottom: 20 }} />
                <div className="sim-box" style={{ width: 384, height: 14, marginBottom: 8, maxWidth: '80%' }} />
                <div className="sim-box" style={{ width: 320, height: 14, marginBottom: 8, maxWidth: '65%' }} />
                <div className="sim-box" style={{ width: 256, height: 14, marginBottom: 32, maxWidth: '50%' }} />

                <div style={{ display: 'flex', gap: 12 }}>
                  <div className="sim-box primary" style={{ width: 128, height: 36, borderRadius: 8 }} />
                  <div className="sim-box" style={{ width: 112, height: 36, borderRadius: 8 }} />
                </div>
              </div>

              {/* Features */}
              <div className="sim-cards">
                <div className="sim-box" style={{ width: 160, height: 16, margin: '0 auto 32px' }} />
                <div className="sim-grid">
                  {[0, 1, 2].map((i) => (
                    <div key={i} className="sim-card">
                      <div className="sim-box" style={{ width: 36, height: 36, borderRadius: 8, background: 'var(--observed-soft)' }} />
                      <div className="sim-box dark" style={{ width: '75%', height: 14 }} />
                      <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                        <div className="sim-box" style={{ width: '100%', height: 10 }} />
                        <div className="sim-box" style={{ width: '83%', height: 10 }} />
                        <div className="sim-box" style={{ width: '66%', height: 10 }} />
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Table */}
              <div className="sim-table-wrap">
                <div className="sim-table">
                  <div className="sim-table-header">
                    <div className="sim-box dark" style={{ width: 112, height: 14 }} />
                    <div className="sim-box" style={{ width: 80, height: 28, borderRadius: 6 }} />
                  </div>
                  {[0, 1, 2, 3].map((i) => (
                    <div key={i} className="sim-table-row">
                      <div className="sim-box" style={{ width: 28, height: 28, borderRadius: '50%' }} />
                      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 4 }}>
                        <div className="sim-box dark" style={{ width: 128, height: 10 }} />
                        <div className="sim-box" style={{ width: 192, height: 8 }} />
                      </div>
                      <div className="sim-box" style={{ width: 64, height: 10 }} />
                      <div
                        className="sim-box"
                        style={{
                          width: 56,
                          height: 20,
                          borderRadius: 20,
                          background: i === 0 ? 'var(--observed-soft)' : i === 1 ? 'var(--amber-soft)' : 'var(--panel-2)',
                        }}
                      />
                      <div className="sim-box" style={{ width: 24, height: 24 }} />
                    </div>
                  ))}
                </div>
              </div>

              {/* Predicted State Badge */}
              <div className="predicted-badge">
                <div className="predicted-badge-inner">
                  <span className="ping-wrapper">
                    <span className="ping-anim" />
                    <span className="ping-dot" />
                  </span>
                  <span>Predicted State · s{step}</span>
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>

      {/* ── Trajectory ── */}
      <div className="trajectory-panel">
        <div className="timeline">
          <span className="timeline-label eyebrow">Trajectory</span>

          <div className="node-active">
            <Icon path={ICON_PATHS.home} size={15} />
          </div>
          <span className="node-label">s0</span>

          <div className="connector">
            <div className="connector-line" />
            <div className="connector-dot" />
          </div>

          {Array.from({ length: MAX_STEP }, (_, idx) => idx + 1).map((i) => {
            const reached = i <= step;
            return (
              <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 8, flexShrink: 0 }}>
                {reached ? (
                  <>
                    <div className="node-active">
                      <span style={{ fontFamily: 'var(--mono)', fontSize: 11, fontWeight: 600 }}>s{i}</span>
                    </div>
                  </>
                ) : (
                  <div className="node-empty">
                    <span>s{i}</span>
                  </div>
                )}
                {i < MAX_STEP && (
                  <div className={`connector ${reached ? '' : 'dim'}`}>
                    <div className="connector-line" />
                    <div className="connector-dot" />
                  </div>
                )}
              </div>
            );
          })}

          <div className="hint-badge">
            <Icon path={ICON_PATHS.plus} size={11} />
            step
          </div>

          <div className="model-info">
            <div className="info-chip">
              <Icon path={ICON_PATHS.cpu} size={12} />
              <span>WebWM-1B</span>
            </div>
            <div className="info-chip">
              <Icon path={ICON_PATHS.monitor} size={12} />
              <span>1024×768</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;