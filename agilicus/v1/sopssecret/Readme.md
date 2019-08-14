## SopsSecret

A very simple SOPS secrets plugin. It takes the output from SOPS and adjusts namespace / name. No further transformations. :)


Example:

```yaml
---
apiVersion: agilicus/v1
kind: SopsSecret
metadata:
  name: mysecret
  namespace: mynamespace
secret_source: mysecret.enc.yaml
```


Generating 2 different secrets from the same source file is also possible:


```yaml
---
apiVersion: agilicus/v1
kind: SopsSecret
metadata:
  name: mysecret
  namespace: mynamespace
secret_source: mysecret.enc.yaml
---
apiVersion: agilicus/v1
kind: SopsSecret
metadata:
  name: mysecret2
  namespace: mynamespace2
secret_source: mysecret.enc.yaml
---
```
