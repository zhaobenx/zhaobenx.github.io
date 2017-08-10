---
layout: post
title: Katex 公式测试
comments: true
tag: ["Test","katex","Comment"]
---

# Katex 测试

## 行内公式
行内公式使用$$ \int u \frac{dv}{dx}\,dx=uv-\int \frac{du}{dx}v\,dx $$ （kramdown 行内公式使用双dollar）
```latex
$$ \int u \frac{dv}{dx}\,dx=uv-\int \frac{du}{dx}v\,dx $$ 
```

这是一些空行。

一些空行


一些空行

一些空行


## 公式块


$$
\begin{aligned}
\dot{x} & = \sigma(y-x) \\
\dot{y} & = \rho x - y - xz \\
\dot{z} & = -\beta z + xy
\end{aligned}
$$

```tex
$$
\begin{aligned}
\dot{x} & = \sigma(y-x) \\
\dot{y} & = \rho x - y - xz \\
\dot{z} & = -\beta z + xy
\end{aligned}
$$
```

一些空行

一些空行

{% raw %}
# gist 内嵌代码测试
一些空行

一些空行

一些空行

一些空行


{% gist 6706249 %}
{% endraw %}
一些空行

一些空行

一些空行

# 代码测试

## python

```python
def hello:
    print("hello world")

```
## C

```c
int main()
{
    printf("hello world");
    return 0;
}
```

一些空行

## 随便语言

```
我们试一试一行最多可以多长吧，究竟能多长呢，让我们拭目以待。还要说些什么呢话都说完了。配置一个博客也真是麻烦呢。还得更长。让我们复制好了。我们试一试一行最多可以多长吧，究竟能多长呢，让我们拭目以待。还要说些什么呢话都说完了。配置一个博客也真是麻烦呢。还得更长。让我们复制好了。
不管了


```