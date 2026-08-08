import Fastify from 'fastify';
import dotenv from 'dotenv';

dotenv.config();

const app = Fastify({
  logger: true
})

app.get('/api_check', async function handler (request, reply) {
  return { status: 202 }
})

app.get('/start_engine', async function handler(request, reply) {


  
})


try {
  await app.listen({ port: 3000 })
} catch (err) {
  app.log.error(err)
  process.exit(1)
}