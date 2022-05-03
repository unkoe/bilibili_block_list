# bilibili_block_list

bilibili 弹幕屏蔽规则

### 使用方式

1. 随机打开一个视频 
2. 弹幕设置 
3. 添加屏蔽词 
4. 在屏蔽文本中导入 `json文件` 即可

### 合并工具

环境：python3

```
python merge <base-path> <head-path> [<Option>]

Option:

  -mode   设置模式，check 或者 merge, 缺省值为merge

```


- 检查是否存在冲突项
    ```
    python merge.py base_bilibili.block.json head_bilibili.block.json -mode=check
    ```
- 合并两个文本对象
    ```
    python merge.py base_bilibili.block.json headn_bilibili.block.json -mode=merge
    ```

