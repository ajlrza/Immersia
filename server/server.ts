import * as os from 'os';
import dotenv from 'dotenv';
import Fastify from 'fastify';
import { FastifyRequest } from 'fastify';
import * as process from 'node:process';
import * as perfMonitor from '../server/services/monitor'
import * as engineInterface from '../src/interfaces/engine_interfaces'
import * as types from '../src/types/state_types'

dotenv.config();

const app = Fastify({
  logger: true
})

type Request = FastifyRequest<{

  Body: { 
    action: any, 
    avatar: types.avatarState, 
    state: types.generalState,
    position: types.positionState,
    world: types.worldState,
    processed: types.avatarStateExt | types.generalStateExt | types.positionStateExt | types.worldStateExt,
  };
  
  Params: { 
    id: string 
  };

}>;

app.get('/api_check', async function handler (request, reply) {
  return { status: 202 }
})

app.get('/engine', async function handler(request: Request, reply) {

  const totalMemory = os.totalmem();
  const freeMemory = os.freemem();
  const usedMemory = totalMemory - freeMemory;

  const memoryUsagePercentage: number = (usedMemory / totalMemory) * 100;

  const enginePayload: engineInterface.enginePayload = {
    Action: request.body.action ?? undefined,
    Avatar: request.body.avatar ?? undefined,
    State: request.body.state ?? undefined,
    Position: request.body.position ?? undefined,
    World: request.body.world ?? undefined,
  }

  const perfPayload: any = {
    engine: enginePayload ?? undefined,
    resourceUsed: memoryUsagePercentage ?? undefined,
    cpuStats: [],
    processedData: request.body.processed ?? undefined,
  }

 if (memoryUsagePercentage >= 85) {
      console.warn(`🚨 DANGER: Memory usage is at ${memoryUsagePercentage.toFixed(2)}%! System may experience severe slowdowns.`)
      perfPayload['cpuStats'] = perfMonitor.getCPUStats("extreme")

  } else if (memoryUsagePercentage >= 70) {
      console.log(`⚠️ WARNING: High memory usage (${memoryUsagePercentage.toFixed(2)}%).`);
      perfPayload["cpuStats"] = perfMonitor.getCPUStats("bad")

  } else {
      console.log(`✅ Healthy: Memory usage is at ${memoryUsagePercentage.toFixed(2)}%.`);
      perfPayload["cpuStats"] = perfMonitor.getCPUStats("normal")
  }

  const response = await fetch('https://immersia_service.com/engine', {
    method: 'POST',
    headers: {
      'User-Agent': 'undici-stream-example',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(perfPayload),
  });

})

try {
  await app.listen({ port: 3000 })
} catch (err) {
  // need a fallback here
  app.log.error(err)
  process.exit(1)
}