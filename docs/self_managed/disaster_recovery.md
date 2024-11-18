# Disaster recovery

## Scenarios and actions

### Accidentally removed/deleted a pod of Lamini Platform from K8s

No action needed. Kubernetes should restart the pod automatically.

### Accidentally removed/delete a secret of Lamini Platform from K8s

Need to recreate the secret. Otherwise redeploy or upgrade Lamini Platform will fail, as it misses the `imagePullSecret`.

### Accidentally delete the whole namespace of Lamini Platform from K8s

Make sure you have pvc achived. Need to first reinstall `persistent-lamini`, restore the content of the newly-created pvc
from the archived pvc, and then reinstall `lamini`.
