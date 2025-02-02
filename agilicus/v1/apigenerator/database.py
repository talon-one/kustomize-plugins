database = """
---
apiVersion: agilicus.com/v1
kind: cockroachdb
metadata:
  name: {cfg[db][name]}
  namespace: {cfg[metadata][namespace]}
spec:
  dbname: {cfg[db][name]}
  user: {cfg[db][user]}
  password: {cfg[db][password]}
"""
