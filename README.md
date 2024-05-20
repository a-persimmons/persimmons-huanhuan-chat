# persimmons-huanhuan-chat
分享 llama-3-8b-instruct 微调一个 嬛嬛 Chat 过程

-  [LLaMA3_8B_Instruct_Lora_huanhuan.ipynb](LLaMA3_8B_Instruct_Lora_huanhuan.ipynb) ：微调过程
-  [Getting_to_know_Llama.ipynb](Getting_to_know_Llama.ipynb) :了解 Llama 3：开始构建所需的一切

## 微调环境

- [算力互联 - 控制台](https://console.casdao.com:9001/#/overview)：4090D-24G

## 微调过程

1. 先充值：5块，新注册后领取5块抵50卷，然后使用，充值

2. 购买机器：

   ![image-20240520191430008](README.assets/image-20240520191430008.png)

   ![image-20240520191547880](README.assets/image-20240520191547880.png)

   根据提示填写端口号，然后直接创建实例![image-20240520191728821](README.assets/image-20240520191728821.png)

3. 回到实例

   ![image-20240520191932438](README.assets/image-20240520191932438.png)

4. 打开实例的 Jupyter

   ![image-20240520192338409](README.assets/image-20240520192338409.png)

5. 双击进入 fssd目录

   ![image-20240520192312496](README.assets/image-20240520192312496.png)

6. 双击 进入终端

   ![image-20240520192436168](README.assets/image-20240520192436168.png)![image-20240520192534174](README.assets/image-20240520192534174.png)

7. 克隆项目

   ```bash
   git clone https://github.com/a-persimmons/persimmons-huanhuan-chat.git
   
   cp persimmons-huanhuan-chat/LLaMA3_8B_Instruct_Lora_huanhuan.ipynb .
   ```

8. 双击打开微调脚本 *LLaMA3_8B_Instruct_Lora_huanhuan.ipynb*

9. 开始微调，按步骤一步一走

10. 下载模型

    单机 这个图标

    ![image-20240520194615691](README.assets/image-20240520194615691.png)

    进入fsas 目录

    ![image-20240520194650036](README.assets/image-20240520194650036.png)

    单机右键 选择下载即可

    ![image-20240520194755209](README.assets/image-20240520194755209.png)

11. 本地部署模型

    1. 安装ollama
