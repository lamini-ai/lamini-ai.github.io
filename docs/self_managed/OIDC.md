## User Authentication with OIDC

Lamini Platform supports [Open ID Connect (OIDC)](https://openid.net/developers/specs/) for user authentication. When enabled, only OIDC-authenticated users are able to access your Lamini instance. When an unauthenticated user tries to access your Lamini instance, they will be redirected to the OIDC identity provider you specify to log in. You can use any vendor-provided OIDC provider (like Auth0, Okta, AWS IAM, GCP Identity Platform, Azure Entra, and many more) or any internal service that adheres to the OIDC standard.

After a user has signed in to Lamini Platform, they can create API keys and authenticate requests as described in [API authentication](../authenticate.md).

### Setup flow

1. Determine the URI where your Lamini Platform instance will run.
1. Create an application in your OIDC provider for Lamini and configure it.
    1. Example configuration: Auth0
        1. Application Type: `Regular Web Application`
        1. Login URL: `https://<LAMINI_INSTANCE_URI>/v1/auth/login`
        1. Callback URL `https://<LAMINI_INSTANCE_URI>/v1/auth/auth`
        1. Logout URL `https://<LAMINI_INSTANCE_URI>`
        1. Web origins `https://<LAMINI_INSTANCE_URI>`
    1. Example configuration: Google
        1. Redirect URI: `https://<LAMINI_INSTANCE_URI>/v1/auth/auth`
        1. Authorized Origin: `https://<LAMINI_INSTANCE_URI>`
1. Get the Application Client ID, Application Client Secret, and the OIDC Connect URL for your OIDC provider.
    1. Example URL: Auth0: `https://<YOUR-AUTH0-APP>/.well-known/openid-configuration`
    1. Example URL: Google: `https://accounts.google.com/.well-known/openid-configuration`
1. Configure OIDC in the `llama_config_edits.yaml` file for your Lamini install
    1. Set `disable_auth` to `False` to enable auth
    ```yaml
    auth:
      disable_auth: False
    ```
    1. Set `website` to the URI of your Lamini Platform instance
    ```yaml
    powerml:
      website: "https://<LAMINI_INSTANCE_URI>"
    ```
    1. Set the `client_id`, `client_secret`, and `server_metadata_url` values
    ```yaml
    auth_provider:
      client_id: "<CLIENT_ID>"
      client_secret: "<CLIENT_SECRET>"
      server_metadata_url: "<OIDC_CONNECT_URL>"
    ```
