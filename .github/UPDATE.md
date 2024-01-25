# ⬆️ Update Document

### Add new feature

- Add folder component `apps/`

```
apis/
- [feature-name]/
    - __init__.py
    - models/
    - controllers/
```

- Register APIRoute `apps/apis/__init__.py`

```python
router.include_router(feature_router)
```

- Add Swagger document `utils/metadata.py`

```python
{
    "name": "task-alias",
    "description": "Description"
}
```

### Add Children Server feature

👉 [Google Colab](https://colab.research.google.com/drive/1pzkxAMOEwPWUqRVHCN_dkgVF2Coj3wmj)

- Add Logic `🤗Logic`

```python
def new_feature_process():
    ...
```

- Add Route `📍Route`

```python
@app.route("/new-feature")
def new_feature():
    ...
    new_feature_process()
```
