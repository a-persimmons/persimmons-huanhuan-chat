import os
from typing import List, Optional

import openai
from dotenv import find_dotenv, load_dotenv
from langchain.llms.base import LLM

_ = load_dotenv(find_dotenv())

# openai.api_key = os.environ["OPENAI_API_KEY"]

# 这里使用 deepseek，自行注册和创建api-key：https://platform.deepseek.com/api_keys
# 其他平台也是如此，前提：这个平台需要兼容openai的api
openai.api_key = "<api_key>"
model_api = "https://api.deepseek.com/v1"


def get_completion(prompt, model="deepseek-chat"):
    '''
    prompt: 对应的提示词
    model: 调用的模型，默认为 gpt-3.5-turbo(ChatGPT)，有内测资格的用户可以选择 gpt-4
    '''
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        api_base=model_api,
        messages=messages,
        temperature=0,  # 模型输出的温度系数，控制输出的随机程度
    )
    # 调用 OpenAI 的 ChatCompletion 接口
    return response.choices[0].message["content"]


class OpenAI_LLM(LLM):
    model_type: str = "openai"

    def __init__(self):
        super().__init__()

    @property
    def _llm_type(self) -> str:
        return "openai"

    def _call(self, prompt: str, history: List = [], stop: Optional[List[str]] = None) -> str:
        res = get_completion(prompt)
        return res

    @property
    def _identifying_params(self):
        """Get the identifying parameters.
        """
        _param_dict = {
            "model": self.model_type

        }
        return _param_dict
