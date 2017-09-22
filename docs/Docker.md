# Docker

## 介紹

Docker 是一種容器 (container) 的技術平台。容器是軟體的封裝，每個容器之間都相互隔離，很像是虛擬機器，但容器不包含整個作業系統，容器比虛擬機器更輕量一些。

Docker 平台是 Client-Server 的架構，由下列元件組成：(參閱 [Docker overview](https://docs.docker.com/engine/docker-overview/))
* Docker 服務 (daemon)：伺服端，負責管理 Docker 的映像檔和容器，也就是 dockerd 指令。
* Docker 映像檔 (image)：容器的樣板 (template)。
* Docker 容器 (container)：可執行的映像檔實體 (instance)。
* Docker 註冊儲存庫 (registry)：儲存映像檔的地方，預設是 [Docker Hub](https://hub.docker.com/) 。
* Docker 用戶端工具 (client)：用戶端，透過 REST API 與 Docker 服務溝通，通常是指 CLI 的 docker 指令。

## docker 指令

所有 docker 指令的詳細內容可參閱 [Use the Docker command line](https://docs.docker.com/engine/reference/commandline/cli/)，以下僅列出指令的意思。

* 列出 docker 指令的基本說明 `docker --help`
* 列出特定 COMMAND 的詳細說明 `docker COMMAND --help`
* 列出版本資訊 `docker --version`
* 列出全系統的資訊 `docker info`
* 列出 Client 與 Server 的詳細版本資訊 `docker version`

### 有關 image 的指令

* `docker build` 從 Dockerfile 建立 image
* `docker commit` 建立 image
* `docker history` 顯示 image 的歷史紀錄
* `docker images` 列出 image
* `docker load` 從 tar 檔或 STDIN 載入 image
* `docker pull` 從 registry 下載 image
* `docker push` 上傳 image 至 registry
* `docker rmi` 刪除 image
* `docker save` 儲存 image 至 tar 檔或 STDOUT
* `docker search` 搜尋 Docker Hub 上面的 image
* `docker tag` 在 image 新增標籤

### 有關 container 的指令

* `docker attach` 附加 STDIN, STDOUT, STDERR 到 container 內
* `docker cp` 在 container 與本機磁碟之間複製檔案或目錄
* `docker create` 建立新的 container
* `docker diff` 顯示 container 與 image 之間的檔案差異
* `docker exec` 在 container 中執行命令
* `docker export` 匯出 container 至 tar 檔
* `docker import` 從 tar 檔匯入 container
* `docker kill` 終結 container
* `docker logs` 顯示 container 的日誌
* `docker pause` 暫停 container
* `docker port` 顯示 container 的連接埠
* `docker ps` 列出 container
* `docker rename` 重新命名 container
* `docker restart` 重新啟動 container
* `docker rm` 刪除 container
* `docker run` 在 container 上執行指令，等於 create 之後 run 。
* `docker start` 啟動 container
* `docker stats` 顯示 container 的資源使用狀態
* `docker stop` 停止 container
* `docker top` 顯示 container 內的 process 資訊
* `docker unpause` 取消暫停 container
* `docker undate` 更新 container 的 configuration
* `docker wait` 等待 container 停止

### 進階指令

* `docker deploy` 部署 stack
* `docker events` 顯示 Docker 服務的事件
* `docker inspect` 檢視 Docker 物件的低階資訊
* `docker login` 登入 Docker registry
* `docker logout` 登出 Docker registry

## docker 管理指令

* `docker checkpoint` 管理 checkpoints
* `docker config` 管理 Docker configs
* `docker container` 管理 containers
* `docker image` 管理 images
* `docker network` 管理 networks
* `docker node` 管理 Swarm nodes
* `docker plugin` 管理 plugins
* `docker secret` 管理 Docker secrets
* `docker service` 管理 services
* `docker stack` 管理 Docker stacks
* `docker swarm` 管理 Swarm
* `docker system` 管理 Docker
* `docker volume` 管理 volumes
