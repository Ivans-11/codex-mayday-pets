# Mayday Pets

![五月天五球宠物预览](preview.gif)

五月天五球主题的 Codex 终端宠物：

- **Ashin** — 阿信
- **Masa** — 玛莎
- **Monster** — 怪兽
- **Stone** — 石头
- **Ming** — 冠佑

## 使用

需要 Python 3、支持宠物的 Codex CLI，以及 Kitty 等支持图片协议的终端。宠物格式适配 Codex CLI 0.166.0。

下载项目后运行，无需安装依赖：

```bash
python3 install.py
```

然后在 Codex 输入 `/pets`，选择对应名字。

默认安装到 `~/.codex/pets/`，支持 `CODEX_HOME` 环境变量。也可指定目录：

```bash
python3 install.py --codex-home /path/to/codex-home
```

已有同名文件内容不同时，安装器会停止；先备份并移走旧版本，再重新安装。
