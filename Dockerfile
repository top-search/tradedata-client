# TradeData Client — Official Docker Container Image
# Multi-platform runtime for CLI trade queries and autonomous AI agents
FROM node:20-alpine AS node-runtime
WORKDIR /app
COPY package*.json ./
RUN npm install --omit=dev
COPY index.js openapi.yaml ./

FROM python:3.11-slim
WORKDIR /app
COPY --from=node-runtime /app /app/node
COPY . /app/python
RUN pip install --no-cache-dir /app/python

ENV NODE_PATH=/app/node/node_modules
ENTRYPOINT ["python3", "-m", "tradedata"]
CMD ["--help"]
