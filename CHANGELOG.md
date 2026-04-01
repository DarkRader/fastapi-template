# Changelog

## [0.1.1](https://github.com/DarkRader/fastapi-template/compare/v0.1.0...v0.1.1) (2026-04-01)


### 🧱 Updates & Improvements

* add create and updated at in base model, fix user schema ([d2e5518](https://github.com/DarkRader/fastapi-template/commit/d2e5518c3279b4a47adf50b3817393e508291219))
* add create bulk operation to base repository, services and api ([be6bfc4](https://github.com/DarkRader/fastapi-template/commit/be6bfc4d197e9de3e26725949793697c08d4e437))
* add fixed migration ([f83f325](https://github.com/DarkRader/fastapi-template/commit/f83f32502a4e693c4a1dc5a5dbca934f72b5cbb9))
* add permissions dependencies at api crud base routers ([bfe2cf5](https://github.com/DarkRader/fastapi-template/commit/bfe2cf5a52253bba0ecbde18ebca19dd97aa8dbe))
* add zed configs to .gitignore ([240e4c0](https://github.com/DarkRader/fastapi-template/commit/240e4c0a758aaaa5431d40a6d473a8367a991618))
* apply migration for updated and created at columns in user ([e5556cc](https://github.com/DarkRader/fastapi-template/commit/e5556cc4c2cb7b323b8ed38ec312ba79dee305ce))
* **build:** do cleaner separation envs in compose ([9368ad4](https://github.com/DarkRader/fastapi-template/commit/9368ad4b95cdc6c3b9e5a06afa59ece61b23eb22))
* **deps:** update dependency pytest-env to v1.6.0 ([5e903df](https://github.com/DarkRader/fastapi-template/commit/5e903df012240aacdf09e5cb96dcf7b833e9f2f3))
* **deps:** update dependency pytest-env to v1.6.0 ([#14](https://github.com/DarkRader/fastapi-template/issues/14)) ([efa39a1](https://github.com/DarkRader/fastapi-template/commit/efa39a157e1793e61ecc3791070d63ec145a0b04))
* **deps:** update ghcr.io/astral-sh/uv docker tag to v0.10.10 ([8106dc5](https://github.com/DarkRader/fastapi-template/commit/8106dc54c3bd2b71442f3af3822c20f48115bd6d))
* **deps:** update ghcr.io/astral-sh/uv docker tag to v0.10.10 ([#17](https://github.com/DarkRader/fastapi-template/issues/17)) ([54cde6e](https://github.com/DarkRader/fastapi-template/commit/54cde6eece86a485c901ecef5952ffe215fbefb9))
* prepare ObjectList feature with proper pagination (not fully) ([8d5bb40](https://github.com/DarkRader/fastapi-template/commit/8d5bb40c2b31c3490f4b4131cea527f0fde12b10))
* remove orjson (Deprecated) ([fd9e297](https://github.com/DarkRader/fastapi-template/commit/fd9e297ed102b9a416b5bd96c2e2aeb179baf40b))


### 🛠️ Fixes

* api base crud ([894cd1f](https://github.com/DarkRader/fastapi-template/commit/894cd1fa8fe8cc6d05d0cc70e69685f9deeed93a))
* dependencies ([f754c8c](https://github.com/DarkRader/fastapi-template/commit/f754c8cb71121bdc8a46bafe4bf282da495ee310))
* **deps:** update dependency pytz to v2026.1.post1 ([66f1a93](https://github.com/DarkRader/fastapi-template/commit/66f1a932e354e1bd7fcbab5237e3dd0ee0004e69))
* **deps:** update dependency pytz to v2026.1.post1 ([#16](https://github.com/DarkRader/fastapi-template/issues/16)) ([4a80f8d](https://github.com/DarkRader/fastapi-template/commit/4a80f8d9413b85be1cc6837c66d532af07112d94))
* generic SchemaLite in service base and user schema ([cb22ad6](https://github.com/DarkRader/fastapi-template/commit/cb22ad60034b2a45b151c14fcf03946220a594d0))
* name object in db (plural) ([e87bec3](https://github.com/DarkRader/fastapi-template/commit/e87bec381fac5ab2bd30254fc96f94db3eca300d))
* OpenIdProviderDep name ([9da88c9](https://github.com/DarkRader/fastapi-template/commit/9da88c99a35536d78a1ae7c376eb4f9d0ddb7f82))
* solve basepyright warnings ([b0f4dcf](https://github.com/DarkRader/fastapi-template/commit/b0f4dcf712ca9cef74dfc544bccd57c115a361fd))


### 🧹 Refactors

* base and user routers (annotated style) ([1d36899](https://github.com/DarkRader/fastapi-template/commit/1d368998a3bf756b14e6446d155b2c2510a55af9))
* base api builder, remove SchemaDetail, left only Schema ([65394cf](https://github.com/DarkRader/fastapi-template/commit/65394cf1a61b0bdbe4de0ba1c2806e74cbd44f20))
* big refactor of ports/adapters pattern ([b45f872](https://github.com/DarkRader/fastapi-template/commit/b45f8721be995695f97613116ec856ee6dbd34d3))
* change base id from str to UUID ([b815849](https://github.com/DarkRader/fastapi-template/commit/b8158492c9c4b215a7c88e37427c16ca662c457d))
* docs strings and fix import for UserServiceDep ([16c3e92](https://github.com/DarkRader/fastapi-template/commit/16c3e9288f83d3e9f2100112a2a26f958ae4872e))
* move db session under infrastructure ([3ff1fc7](https://github.com/DarkRader/fastapi-template/commit/3ff1fc7cfeeab0eea4fc2a87d844c44283c48cc3))
* move models and shemas under domain module ([3566d56](https://github.com/DarkRader/fastapi-template/commit/3566d56f6c0b881c1d40fd365be86b3452c5615b))
* settings config - add APP section ([efb1818](https://github.com/DarkRader/fastapi-template/commit/efb1818e4fb01ef9aad169ad0714bf8b78731cca))

## [0.1.0](https://github.com/DarkRader/fastapi-template/compare/v0.0.1...v0.1.0) (2026-03-07)


### ✨ New Features

* add first src template ([fc72f45](https://github.com/DarkRader/fastapi-template/commit/fc72f457adfeaed51da342966cf8d21dccf8ad41))
* Add proper OpenID auth with authlib + add User Model migration ([c295ba2](https://github.com/DarkRader/fastapi-template/commit/c295ba23da943d2fc145a1ac7e305b4a757229a2))


### 🧱 Updates & Improvements

* add configs for tools and update Dockerfile ([6cf43eb](https://github.com/DarkRader/fastapi-template/commit/6cf43eb49aec3e5ef624775ff542e966c6aea51f))
* add gitignore file ([3c0b082](https://github.com/DarkRader/fastapi-template/commit/3c0b0829fbc59ff68961fbb3425706e6a297f1fa))
* add pre-commit config ([bc4a533](https://github.com/DarkRader/fastapi-template/commit/bc4a5337f078a8c4bd2779fd67789f3f7231f9f8))
* add release please workflow ([77bf11b](https://github.com/DarkRader/fastapi-template/commit/77bf11b5e334fcfae6e36a8017a9b4e171a6566f))
* add renovate config ([a22963d](https://github.com/DarkRader/fastapi-template/commit/a22963d7e63c1cc296da7bca3ad3a93d0c9f56ef))
* add root init projects stuff ([ff546d4](https://github.com/DarkRader/fastapi-template/commit/ff546d403a57eabf189b763d5693414aa1fdf3ca))
* add scripts for create and upgrade venv ([e81e869](https://github.com/DarkRader/fastapi-template/commit/e81e86995e807f6ecb81ebe835e718d60f038650))
* add shemas and models layers ([edeb743](https://github.com/DarkRader/fastapi-template/commit/edeb743d85a49796936bb2b1471327402bc6c4de))
* add well known endpoints, some small fixes in another endpoints ([265d724](https://github.com/DarkRader/fastapi-template/commit/265d724a91d744937f0417fde537bca0289aed4d))
* **build:** update Dockerfile ([4deb515](https://github.com/DarkRader/fastapi-template/commit/4deb515f9ab9d1e6ffb6fcf2d6b0089dad621e5f))
* **deps:** update dependency ruff to v0.15.4 ([7852b98](https://github.com/DarkRader/fastapi-template/commit/7852b98a0638590872ea3b5861e2f80d9363a889))
* **deps:** update dependency ruff to v0.15.4 ([7852b98](https://github.com/DarkRader/fastapi-template/commit/7852b98a0638590872ea3b5861e2f80d9363a889))
* **deps:** update dependency ruff to v0.15.4 ([3f3d28d](https://github.com/DarkRader/fastapi-template/commit/3f3d28d34ac0c0639e361b9c9bee1a059f59402e))
* refactor, update deps and dockerfile ([6b627d0](https://github.com/DarkRader/fastapi-template/commit/6b627d0f487953b332e6c5401204b61ee4842f34))
* **renovate:** update config, apply automerge for minor and patch ([47fad5d](https://github.com/DarkRader/fastapi-template/commit/47fad5d84885fad13478c72ab3a4ffcbb58458e7))
* **renovate:** update config, apply platformAutomerge ([596b28c](https://github.com/DarkRader/fastapi-template/commit/596b28ca533871deed77274aacb445074f495804))
* **ruff:** format ([8320083](https://github.com/DarkRader/fastapi-template/commit/8320083b5598ad5d0726b2a532d01a6d283b00a8))


### 🛠️ Fixes

* base branch ([ea75477](https://github.com/DarkRader/fastapi-template/commit/ea7547742acc6176fd070d8a6881a3cc53199138))
* **deps:** update dependency aiohttp to v3.13.3 ([45f9ee1](https://github.com/DarkRader/fastapi-template/commit/45f9ee1f3ed03f2f1c9e1f8c69762ed795b1bd8f))
* **deps:** update dependency aiohttp to v3.13.3 ([45f9ee1](https://github.com/DarkRader/fastapi-template/commit/45f9ee1f3ed03f2f1c9e1f8c69762ed795b1bd8f))
* **deps:** update dependency aiohttp to v3.13.3 ([313120c](https://github.com/DarkRader/fastapi-template/commit/313120c4e4049d8fd26f7b4e3245367440a3ac5e))
* **deps:** update dependency alembic to v1.18.4 ([54744bc](https://github.com/DarkRader/fastapi-template/commit/54744bc8548309690070c9ee1b90d7b037bbb572))
* **deps:** update dependency alembic to v1.18.4 ([54744bc](https://github.com/DarkRader/fastapi-template/commit/54744bc8548309690070c9ee1b90d7b037bbb572))
* **deps:** update dependency alembic to v1.18.4 ([2181348](https://github.com/DarkRader/fastapi-template/commit/21813483d680ec3052b21ba5f30aad84848d9f3b))
* **deps:** update dependency authlib to v1.6.9 ([d22e505](https://github.com/DarkRader/fastapi-template/commit/d22e505eef9d46db9e3ca73903eaf77929e61408))
* **deps:** update dependency authlib to v1.6.9 ([d22e505](https://github.com/DarkRader/fastapi-template/commit/d22e505eef9d46db9e3ca73903eaf77929e61408))
* **deps:** update dependency authlib to v1.6.9 ([6be8e7f](https://github.com/DarkRader/fastapi-template/commit/6be8e7ff504da2afb06dba83bfd13021d27d9371))
* **deps:** update dependency orjson to v3.11.7 ([7c0e7cb](https://github.com/DarkRader/fastapi-template/commit/7c0e7cb8df7c4a40432bb0474db00ba771e34916))
* **deps:** update dependency orjson to v3.11.7 ([7c0e7cb](https://github.com/DarkRader/fastapi-template/commit/7c0e7cb8df7c4a40432bb0474db00ba771e34916))
* **deps:** update dependency orjson to v3.11.7 ([ac9e8da](https://github.com/DarkRader/fastapi-template/commit/ac9e8da72a361b2dd940459a57a9d2d2439fdecf))
* **deps:** update dependency sqlalchemy to v2.0.47 ([375db5c](https://github.com/DarkRader/fastapi-template/commit/375db5ccdbeedeeaeb8cb2b40b9b783844f4d0b6))
* **deps:** update dependency sqlalchemy to v2.0.47 ([375db5c](https://github.com/DarkRader/fastapi-template/commit/375db5ccdbeedeeaeb8cb2b40b9b783844f4d0b6))
* **deps:** update dependency sqlalchemy to v2.0.47 ([b87f77c](https://github.com/DarkRader/fastapi-template/commit/b87f77c16c8a1d9112a840c9f613460046679064))
* pre-commit fixes ([2e887af](https://github.com/DarkRader/fastapi-template/commit/2e887afd339ca8940ad6cd0dcbb493234251169c))
* WellKnownResponse schema ([83301f4](https://github.com/DarkRader/fastapi-template/commit/83301f4bdcb2bd2ea261c1e3ebf3c7776938f292))


### 🧹 Refactors

* add package adapter for external services + rename docker-compose to compose ([24d0613](https://github.com/DarkRader/fastapi-template/commit/24d0613193eff8119ec22062eb91f86dffb4d6ee))
* restructure project move all stuff related to python project under fastapi-app folder ([753ae74](https://github.com/DarkRader/fastapi-template/commit/753ae742460684edde11007aaaa22ab38bc336e3))
* solve ruff add .env.example, compose.yaml ([d7e54e6](https://github.com/DarkRader/fastapi-template/commit/d7e54e68fc834ac0db77c1b6fbbf47b3ead757ea))
* solve ruff and mypy warnings ([823cb6d](https://github.com/DarkRader/fastapi-template/commit/823cb6dcd0459a9f10ef510bd194d1c6c9a10e9d))


### 📝 Documentation

* add get started instruction to README ([d258adb](https://github.com/DarkRader/fastapi-template/commit/d258adb4c30ca9d8312b8c9a99ed947123799d31))
