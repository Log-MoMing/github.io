# MkDocs模板

这是一个MkDocs模板，可以快速搭建并部署个人博客网页到GitHub Pages。

- Material 主题 （安装了 [Material for MkDocs](https://github.com/squidfunk/mkdocs-material)）
- 支持Jupyter笔记 （安装了 [mkdocs-jupyter](https://github.com/danielfrg/mkdocs-jupyter)）
- 评论系统（根据 Material 教程搭建）
- 博客（根据 Material 教程搭建）
- 亮色/深色/跟随系统 模式切换（根据 Material 教程搭建）
- 个人认为比较好看的样式添加及调整（根据 Material 教程搭建）


## 评论系统

> 官方教程:  [添加评论系统](https://squidfunk.github.io/mkdocs-material/setup/adding-a-comment-system/)

[comments.html 跳转](overrides/partials/comments.html)

如果不需要为博客中的帖子添加评论系统，可以直接删除`overrides/partials/comments.html`文件。

如果需要为博客中的帖子添加评论系统，请将从 `giscus` 中复制的包含配置信息的 script 标签 粘贴到 `overrides/partials/comments.html` 中的提示位置


## 博客

> 官方教程: [设置博客(https://squidfunk.github.io/mkdocs-material/setup/setting-up-a-blog/)]

这里不再赘述，具体查看官方教程即可。

下方仅列出本模板中需要改动的部分。

### 1. 作者信息

[跳转至 `docs/blog/.authors.yml` ](docs/blog/.authors.yml)

### 2. 模板帖
[跳转至 `docs/blog/posts/hello_world.md` ](docs/blog/posts/hello_world.md#博客示例贴你好-世界)
