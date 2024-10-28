# yagsvc: yag macroservice

## Test

You need to use "localhost" as OAuth providers wouldn't work with other domains.

1. Run yag-mcc
2. Open http://localhost:8080/api/, logout if needed
3. Login using any auth method
4. Now you can trigger API calls from http://localhost:8080/api/docs/

## Swagger UI

    git clone --depth=1 --single-branch --branch "master" https://github.com/swagger-api/swagger-ui.git /tmp/swagger-ui
    cp /tmp/swagger-ui/dist/*.css /workspaces/yagsvc/yagsvc/static/css
    cp /tmp/swagger-ui/dist/*.png /workspaces/yagsvc/yagsvc/static/img
    cp /tmp/swagger-ui/dist/*.js /workspaces/yagsvc/yagsvc/static/js
    cp /tmp/swagger-ui/dist/index.html /workspaces/yagsvc/yagsvc/templates/swaggerui.html

Then modify:
    templates/swaggerui.html
    js/swagger-initializer.js
