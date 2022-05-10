# Docker Commands

## Vaultwarden

sudo docker run -d --name vaultwarden --net main --ip 172.18.0.3 -v /vw-data/:/data/ \
    -e DOMAIN=https://446256.xyz/4e7emr39k798api9trti9ncfdinhki2y/ \
    -e SIGNUPS_ALLOWED=false -e INVITATIONS_ALLOWED=false \
    -e ADMIN_TOKEN=I2tfdGUTzKSMjYjcX3eU6sS64gvksR2OW1L/qNEg8PQo4X7qW5l51MrTk46ih/Jx \
    -e WEBSOCKET_ENABLED=true -e SMTP_HOST=smtp.gmail.com \
    -e SMTP_FROM=risainasaka@gmail.com -e SMTP_PORT=587 -e SMTP_SSL=true \
    -e SMTP_EXPLICIT_TLS=false -e SMTP_USERNAME=risainasaka@gmail.com \
    -e SMTP_PASSWORD=olljubupkuebjtex -e SHOW_PASSWORD_HINT=false \
    vaultwarden/server:latest
