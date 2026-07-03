# Seguridad

## Credenciales y API keys

1. **Ninguna credencial se versiona en git.** Nunca. `.env`, claves, tokens y seeds están en `.gitignore` y se verifica antes de cada commit.
2. Las API keys de exchange se crean con los **permisos mínimos**: trading habilitado, **retiros deshabilitados**, restricción por IP cuando sea posible.
3. Claves separadas por entorno: testnet y producción nunca comparten credenciales.
4. Las claves se almacenan fuera del repo (variables de entorno o gestor de secretos local) y se rotan tras cualquier sospecha de exposición.

## Repositorio

- El repositorio es privado. Antes de cualquier cambio de visibilidad, auditar el historial completo en busca de secretos.
- Si una credencial llega a un commit (aunque sea privado): se revoca inmediatamente en el exchange y luego se limpia el historial. Revocar primero, limpiar después.

## Pendiente

- [ ] Documentar el mecanismo concreto de carga de secretos cuando se migre el bot.
- [ ] Checklist de seguridad previo a Fase C (capital real).
