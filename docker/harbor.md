# harbor

## 常用命令

```bash
USER_NAME='admin'
USER_PASSWORD='123456'
REPO_HOSTNAME='harbor.xxx.com'

# 删除仓库
curl -u "${USER_NAME}:${USER_PASSWORD}" -X DELETE -H "Content-Type: application/json" http://${REPO_HOSTNAME}/api/v2.0/projects/project_name/repositories/repo1

# 根据tag打tag
curl -u "${USER_NAME}:${USER_PASSWORD}" -X POST -H "Content-Type: application/json" -d '{"name": "hi"}' http://${REPO_HOSTNAME}/api/v2.0/projects/project_name/repositories/repo1/artifacts/1.0.0/tags

# 列出所有的tag
curl -u "${USER_NAME}:${USER_PASSWORD}" -X GET -H "Content-Type: application/json"  http://${REPO_HOSTNAME}/api/v2.0/projects/project_name/repositories/repo1/artifacts/1.0.0/tags
/projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/tags
```

