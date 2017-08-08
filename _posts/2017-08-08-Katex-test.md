---
layout: post
title: Katex 公式测试
comments: true
---

* TOC
{:toc}
# Katex 测试

行内公式$$ \int u \frac{dv}{dx}\,dx=uv-\int \frac{du}{dx}v\,dx $$ （kramdown 行内公式使用双dollar）

公式：


$$
\begin{aligned}
\dot{x} & = \sigma(y-x) \\
\dot{y} & = \rho x - y - xz \\
\dot{z} & = -\beta z + xy
\end{aligned}
$$

# gist 内嵌代码测试

{% gist 6706249 %}

# python代码测试

```python
def hello:
    print("hello world")
```

