adlsAccount = "enter your account name"
adlsContainer = "enter your container name"
adlsFolder = "enter foler name"

applicationId = "enter application(client)ID"  OR  dbutils.secrets.get(scope="your scope",key="your key")
applicationKey = dbutils.secrets.get(scope="your scope",key="your key")
tenantId = dbutils.secrets.get(scope="your scope",key="your key")

endpoint = "https://login.microsoftonline.com/" + tenantId + "/oauth2/token"
source = "abfss://" + adlsContainer + "@" + adlsAccount + ".dfs.core.windows.net/" + adlsFolder

#Option 1 -- Connecting using Service Principal secrets and OAuth
configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": applicationId,
           "fs.azure.account.oauth2.client.secret": applicationKey,
           "fs.azure.account.oauth2.client.endpoint": endpoint}

# Option 2 or optional loop
# Mount ADLS to DBFS only if directory has not been mounted
if not any(mount.mountPoint == mountPoint for mount in dbutils.fs.mounts()):
  dbutils.fs.mount(
    source = source,
    mount_point = mountPoint,
    extra_configs = configs)
