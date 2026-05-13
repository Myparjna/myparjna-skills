# Deployment Platforms

Use this file when the project clearly targets one platform or deployment mode.

## Vercel

- Document production environment variables in the dashboard.
- Include the build command, output directory, and domain binding steps.

## Netlify

- Include build command, publish directory, and environment variable setup.
- Mention preview and production branch behavior if used.

## Docker

- Include `docker build`, image tag strategy, registry target, and runtime command.
- Document volumes, ports, and secret injection.

## Kubernetes

- Include namespaces, manifests or Helm chart locations, config maps, secrets, ingress, and rollback commands.

## VPS / bare server

- Document process manager, reverse proxy, SSL, deploy directory, and restart procedure.
