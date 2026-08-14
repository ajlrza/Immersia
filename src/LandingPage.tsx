import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router';
import * as Engine from './services/engine_request'
import './LandingPage.css';

const ICON_STROKE = 1.75;

function Icon({ path = "", size = 16 }) {
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
  world: 'M12 3l8 4.5v9L12 21l-8-4.5v-9L12 3z',
  bolt: 'M13 10V3L4 14h7v7l9-11h-7z',
  cursor: 'M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5',
  play: 'M5 3l14 9-14 9V3z',
  cpu: 'M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z',
  monitor: 'M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z',
  scroll: 'M7 16V4m0 0L3 8m4-4l4 4m6 0v12m0 0l4-4m-4 4l-4-4',
  eye: 'M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5C21.27 7.61 17 4.5 12 4.5zM12 16.5a4.5 4.5 0 110-9 4.5 4.5 0 010 9z',
  eyeOff: 'M3 3l18 18M10.6 10.6a2.25 2.25 0 003.18 3.18M9.88 4.68A10.6 10.6 0 0112 4.5c5 0 9.27 3.11 11 7.5a13.2 13.2 0 01-3.29 4.61M6.3 6.3A13.2 13.2 0 001 12c1.05 2.66 3 4.85 5.44 6.2',
};

const MODES = [
  { id: 'interact', label: 'Interact', icon: ICON_PATHS.cursor },
  { id: 'generate', label: 'Generate', icon: ICON_PATHS.world },
  { id: 'observe', label: 'Observe', icon: ICON_PATHS.cpu },
];

const FEATURES = [
  {
    icon: ICON_PATHS.cursor,
    color: 'violet',
    title: 'Act on the world',
    desc: 'Click, type, or scroll — every action space is native to the model, no scripted browser underneath.',
  },
  {
    icon: ICON_PATHS.cpu,
    color: 'teal',
    title: 'Read the state back',
    desc: 'Inspect the predicted DOM tree, accessibility tree, or bounding boxes for anything on screen.',
  },
  {
    icon: ICON_PATHS.scroll,
    color: 'amber',
    title: 'Walk the trajectory',
    desc: 'Every predicted state chains onto the last, so you can branch, rewind, or replay a full session.',
  },
];

const HINTS = [
  'Open a pricing page and click the Pro plan',
  'Scroll to the footer of a blog',
  'Fill out a signup form',
];


function initiateProcess(event: React.MouseEvent<HTMLButtonElement, MouseEvent> | React.SubmitEvent<HTMLFormElement>): Boolean {

  event.preventDefault();
  // Check if anything was sent
  const eventMetadata: any | undefined = event.timeStamp || event.type;

  const formEl = event.target as HTMLFormElement;
  const submittedPrompt = formEl.elements.namedItem('prompt-field') as HTMLTextAreaElement;
  const submittedAPIKey = formEl.elements.namedItem('api-field') as HTMLTextAreaElement;

  let dateNow = new Date()

  let metadataPayload: object = {
      "Timestamp": eventMetadata
  };

  const invalidPrompts: object = {
    "": true,
    "undefined": true
  }

  const spaceExtract = submittedPrompt.match("") ?? "undefined";

  if (typeof spaceExtract === "undefined" && invalidPrompts[spaceExtract]) {
      console.log("Possible gibberish prompt detected")
      return false
  }

  if (submittedPrompt == "" && invalidPrompts[""]) {
      console.log("No prompt detected")
      return false
  }

  if (typeof eventMetadata === "undefined" && submittedPrompt != "undefined") {
      console.log("Submitted but no event recorded")
      
      metadataPayload = {
        "Date": dateNow.getDate,
        "Time": dateNow.getTime
      }
  }

  if (typeof submittedPrompt === undefined) {
    alert("No prompt detected");
    return false;
  }

  const engineRequest = Engine.processPromptWorld({"metadata": metadataPayload, "prompt": submittedPrompt, "model": submittedAPIKey})

  return true;

}

function LandingPage() {
  const [activeMode, setActiveMode] = useState('interact');
  const [prompt, setPrompt] = useState('');
  const [sessionStarted, startSession] = useState(false);
  const [showKey, setShowKey] = useState(false);

  if (sessionStarted === true) {

    const sessionID = Math.floor(Math.random() * 10)
    document.cookie = `Cookie=${sessionID}; path=/;`;

  }

  let navigate = useNavigate();

  useEffect(() => {

    if (sessionStarted) {
      const sessionID = Math.floor(Math.random() * 10);
      document.cookie = `Cookie=${sessionID}; path=/;`;

      navigate("/home");
    }
  }, [sessionStarted, navigate]);

  return (
    <div className="landing">
      <div className="landing-wrap">
        <nav className="landing-nav">
          <div className="landing-brand">
            <div className="landing-brand-mark">
              <Icon path={ICON_PATHS.world} size={16} />
            </div>
            <span className="landing-brand-name">
              Immersia<sup className="landing-brand-sup">v0.1</sup>
            </span>
          </div>
          <div className="landing-nav-links">
            <a href="#">Model</a>
            <a href="#">Docs</a>
            <a href="#">Research</a>
            <a href="#">Pricing</a>
          </div>
          <button className="landing-nav-cta">
            <Icon path={ICON_PATHS.bolt} size={14} />
            Launch console
          </button>
        </nav>

        <div className="hero-img-one">
          <image>
            <img src="https://i.pinimg.com/736x/f2/a8/84/f2a8840d1eaebef65a3d86ad573aaf26.jpg"></img>
          </image>
        </div>

        <div className="hero-img-two">
          <image>
            <img src="https://i.ytimg.com/vi/M1VWSk7xrQU/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLA0HVlTiRX5wubkBInZXWcrr5zcNg"></img>
          </image>
        </div>

        <section className="landing-hero">
          <div className="landing-eyebrow">
            <span className="landing-eyebrow-dot" />
            Generate isekai worlds with dynamic context and persistent states!
          </div>

          <h1 className="landing-h1">
            Immerse
            <br />
            inside your <span className="landing-accent">dream world</span>
          </h1>
          <p className="landing-sub">
            Immersia is a generative AI application powered by web world models. Describe a world with lore, characters, settings, and
            other visuals — it creates the world where you're not the main character, but a character amongst characters.
          </p>

          <form onSubmit={(event) => {initiateProcess(event) && startSession(true)}} className="prompt-shell">
            <div className="prompt-chrome">
              <div className="chrome-dots">
                <span />
                <span />
                <span />
              </div>
              <div className="chrome-address">
                immersia://world · <b>generated world s0</b>
              </div>
              <div className="chrome-status">
                <span className="ping-wrapper">
                  <span className="ping-anim" />
                  <span className="ping-dot" />
                </span>
                Awaiting prompt
              </div>
            </div>

            <div className="prompt-body">
              <textarea
                className="prompt-field"
                rows={2}
                placeholder="Describe a world"
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
              />
            </div>

            <label className="key-row" htmlFor="api-field">
              <span className="key-row-icon">
                <Icon path={ICON_PATHS.lock} size={14} />
              </span>
              <span className="key-row-label">API Key</span>
              <input
                id="api-field"
                name="api-field"
                type={showKey ? 'text' : 'password'}
                className="key-input"
                placeholder=""
                autoComplete="off"
                spellCheck={false}
              />
              <button
                type="button"
                className="key-toggle"
                onClick={() => setShowKey((v) => !v)}
                aria-label={showKey ? 'Hide API key' : 'Show API key'}
              >
                <Icon path={showKey ? ICON_PATHS.eyeOff : ICON_PATHS.eye} size={14} />
              </button>
              <span className="key-badge">BYOK</span>
            </label>

            <div className="prompt-footer">
              <div className="mode-chips">
                {MODES.map((mode) => (
                  <div
                    key={mode.id}
                    className={`mode-chip ${activeMode === mode.id ? 'is-active' : ''}`}
                    onClick={() => setActiveMode(mode.id)}
                  >
                    <Icon path={mode.icon} size={13} />
                    {mode.label}
                  </div>
                ))}
              </div>
              <button type="submit" className="run-btn">
                <Icon path={ICON_PATHS.play} size={14} />
                Start
              </button>
            </div>
          </form>

          <div className="prompt-hints">
            {HINTS.map((hint) => (
              <div key={hint} className="hint-pill" onClick={() => setPrompt(hint)}>
                "{hint}"
              </div>
            ))}
          </div>
        </section>

        <div className="trust-row">
          <div className="trust-item">
            <Icon path={ICON_PATHS.cpu} size={14} />
            BYOK - Bring Your Own Keys
          </div>
          <div className="trust-item">
            <Icon path={ICON_PATHS.monitor} size={14} />
            1024×768 native resolution
          </div>
          <div className="trust-item">
            <Icon path={ICON_PATHS.scroll} size={14} />
            Unbounded rollout length
          </div>
        </div>

        <section className="landing-section">
          <div className="section-head">
            <div className="section-eyebrow">HOW IT WORKS</div>
            <div className="section-title">One prompt, an entire anime-like immersive world</div>
          </div>

          <div className="landing-grid">
            {FEATURES.map((feature) => (
              <div key={feature.title} className="landing-card">
                <div className={`card-icon ${feature.color}`}>
                  <Icon path={feature.icon} size={18} />
                </div>
                <h3>{feature.title}</h3>
                <p>{feature.desc}</p>
              </div>
            ))}
          </div>
        </section>

        <footer className="landing-footer">
          <div className="footer-left">
            <Icon path={ICON_PATHS.world} size={14} />
            Immersia — an immersive experience
          </div>
          <div className="footer-links">
            <a href="#">Model card</a>
            <a href="#">Changelog</a>
            <a href="#">Contact</a>
          </div>
        </footer>
      </div>
    </div>
  );
}

export default LandingPage;