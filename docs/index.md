# 欢迎来到 MkDocs!

前往 `mkdocs` 官方教程: [mkdocs.org](https://www.mkdocs.org).

前往 `materia` 教程: [mkdocs-materia](https://squidfunk.github.io/mkdocs-material/getting-started/)

**前往我的笔记花园: [LogDancer 的笔记花园](https://LogDancer.github.io)**

## 模板简介

- Material 主题 （安装了 [Material for MkDocs](https://github.com/squidfunk/mkdocs-material)）
- 支持 Jupyter 笔记 （安装了 [mkdocs-jupyter](https://github.com/danielfrg/mkdocs-jupyter)）
- 评论系统（根据 Material 教程搭建）
- 博客（根据 Material 教程搭建）
- 亮色/深色/跟随系统 模式切换（根据 Material 教程搭建）
- 个人认为比较好看的样式添加及调整（根据 Material 教程搭建）
- 使 `Jupyter` 中的输出部分支持折叠、复制、滚动
  - 折叠可以双击文字，或者单击右上角的折叠按钮
  - 展开可以单击提示文字，或者单击右上角的折叠按钮
  - 复制可以单击右上角的复制按钮
    ![jupyter_custom_button](./images/jupyter_custom_button.png)

## 命令介绍

- `mkdocs new [项目名称]` - 创建一个项目，如果 `项目名称` 为 `.` 则默认为当前目录.
- `mkdocs serve` - 启动一个 live-reloading 的服务器，自动刷新页面.
- `mkdocs build` - 构建项目，生成 `site` 目录.
- `mkdocs -h` - 显示帮助信息.

## 项目结构

    mkdocs.yml    # 主要的配置文件.
    docs/ # 存放文档的目录
        index.md  # 这个文件是网站的主页.
        ...       # 其他的 markdown 文件，或者其他存放文档/图片/视频/音频的文件夹.

**具体请查看 mkdocs.yml 文件内容**
