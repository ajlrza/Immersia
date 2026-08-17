import * as os from 'os';
import dotenv from 'dotenv';
import Fastify from 'fastify';
import * as process from 'node:process';
import * as perfMonitor from '../server/services/perf_monitor'
import * as engineInterface from '../src/interfaces/engine_interfaces'


dotenv.config();

const app = Fastify({
  logger: true
})

app.get('/api_check', async function handler (request, reply) {
  return { status: 202 }
})

app.get('/engine', async function handler(request, reply) {

  const enginePayload: engineInterface.enginePayload = {
    username: request.body.content.username ?? undefined,
    userAction: request.body.content.action ?? undefined,
    datetime: request.body.content.datetime ?? undefined,
  }

  const perfPayload: object = {
    engine: enginePayload ?? undefined,
    resource_used: memoryUsagePercentage ?? undefined,
    processed_data: request.body.content.data ?? undefined,
  }

  const response = await fetch('https://immersia_service.com/engine', {
    method: 'POST',
    headers: {
      'User-Agent': 'undici-stream-example',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(perfPayload),
  });

  const data = await response.json();
  console.log(data);

  const totalMemory = os.totalmem();
  const freeMemory = os.freemem();
  const usedMemory = totalMemory - freeMemory;

  const memoryUsagePercentage: number = (usedMemory / totalMemory) * 100;

  if (memoryUsagePercentage >= 85) {
    console.warn(`🚨 DANGER: Memory usage is at ${memoryUsagePercentage.toFixed(2)}%! System may experience severe slowdowns.`)
    perfPayload["cpuStats"] = perfMonitor.getCPUStats("extreme")

  } else if (memoryUsagePercentage >= 70) {
      console.log(`⚠️ WARNING: High memory usage (${memoryUsagePercentage.toFixed(2)}%).`);
      perfPayload["cpuStats"] = perfMonitor.getCPUStats("bad")

  } else {
      console.log(`✅ Healthy: Memory usage is at ${memoryUsagePercentage.toFixed(2)}%.`);
      perfPayload["cpuStats"] = perfMonitor.getCPUStats("normal")
  }

})

try {
  await app.listen({ port: 3000 })
} catch (err) {
  // need a fallback here
  app.log.error(err)
  process.exit(1)
}