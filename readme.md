
> 注：当前项目为 Serverless Devs 应用，由于应用中会存在需要初始化才可运行的变量（例如应用部署地区、函数名等等），所以**不推荐**直接 Clone 本仓库到本地进行部署或直接复制 s.yaml 使用，**强烈推荐**通过 `s init ${模版名称}` 的方法或应用中心进行初始化，详情可参考[部署 & 体验](#部署--体验) 。

# start-audio-extraction-auth 帮助文档
<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-audio-extraction-auth&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-audio-extraction-auth" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-audio-extraction-auth&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-audio-extraction-auth" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-audio-extraction-auth&type=packageDownload">
  </a>
</p>

<description>

音频提取+鉴权

</description>

<codeUrl>

- [:smiley_cat: 代码](https://github.com/devsapp/start-huggingface/tree/main)

</codeUrl>
<preview>

- [:eyes: 预览](https://github.com/devsapp/start-huggingface/tree/main)

</preview>


## 前期准备

使用该项目，您需要有开通以下服务并拥有对应权限：

<service>



| 服务/业务 |  权限  | 相关文档 |
| --- |  --- | --- |
| 函数计算 |  AliyunFCFullAccess | [帮助文档](https://help.aliyun.com/product/2508973.html) [计费文档](https://help.aliyun.com/document_detail/2512928.html) |

</service>

<remark>



</remark>

<disclaimers>

免责声明：   
本项目会将模型下载到NAS，并且使用函数计算的GPU实例，模型的大小会影响文件存储占用以及函数执行时间，需根据情况具验证模型下载及加载所产生的费用。

</disclaimers>

## 部署 & 体验

<appcenter>
   
- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=start-audio-extraction-auth) ，
  [![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=start-audio-extraction-auth) 该应用。
   
</appcenter>
<deploy>
    
- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
  - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://docs.serverless-devs.com/fc/config) ；
  - 初始化项目：`s init start-audio-extraction-auth -d start-audio-extraction-auth`
  - 进入项目，并进行项目部署：`cd start-audio-extraction-auth && s deploy -y`
   
</deploy>

## 案例介绍

<appdetail id="flushContent">

本案例支持将提取音频中的文件，并进行请求级别鉴权，采用预先设置token方式。

本案例默认使用huggingface中openai/whisper-base模型进行提取，当然你也可以替换该模型，使用huggingface中Automatic Speech Recognition分类下的模型

本模版优势：
1、自带鉴权功能，支持用户安全访问 
 2、一键拉起huggingface对应的模型，用户不需要关心模型的下载开箱即用

</appdetail>

## 使用流程

<usedetail id="flushContent">

### api调用
只支持POST请求<br>
POST  /  <br>
#### request 
##### header
鉴权：需要再header中添加token， header= {"token":"123456"}<br>
##### body
| 参数                      | 类型                    |
|------------------------------------|-------------------------------------|
| input               | string             |

#### response
| 参数                      | 类型                    |
|------------------------------------|-------------------------------------|
| data              | object             |
| data.text             | string             |
#### 示例
```python
import requests
import json

url = "http://huggingface-audio-gir1.fcv3.1041759428116431.cn-shanghai.fc.devsapp.net"
headers = {"token":"123456"}
s = json.dumps({
    "input": "https://sd-api-demo.oss-cn-beijing.aliyuncs.com/public/1.flac",
})
r = requests.post(url, data=s, headers=headers)
output = r.json()
```
```
{
    "data": {
        "text": "He hoped there would be stew for dinner, turnips and carrots and bruised potatoes and fat mutton pieces to be ladled out in thick, peppered flour-fatten sauce."
    }
}
```

</usedetail>

## 注意事项

<matters id="flushContent">

该案例涉及到使用huggingface模型，由于国内网络不同，采用huggingface镜像站模型数据

</matters>


<devgroup>


## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">  

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <center>微信公众号：`serverless`</center>                                                                                         | <center>微信小助手：`xiaojiangwh`</center>                                                                                        | <center>钉钉交流群：`33947367`</center>                                                                                           |
</p>
</devgroup>
