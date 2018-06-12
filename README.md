# Beginning

Basic utils for Python

## APIS

### operator.slices

有时候我们想对一个序列进行多次切片操作，比如从 `2018-06-12 11:22:33` 中分别取出年、月、日、时、分、秒。通常的方法是这样子的：

```
now = '2018-06-12 11:22:33'
y, m, d, H, M, S = now[0:4], now[5:7], now[8:10], now[11:13], now[14:16], now[17:19]
```

使用 slices 时可以写成这样（注意 `slices` 后面是中括号 `[]`）：

```
y, m, d, H, M, S = slices[0:4, 5:7, 8:10, 11:13, 14:16, 17:19](now)
```

### operator.cut

有时候的需求很简单，就是用 n 个整数把一个序列分成 n+1 个部分。比如从 `20180612112233` 中分别取出年、月、日、时、分、秒。通常的方法是这样子的：

```
now = '20180612112233'
y, m, d, H, M, S = now[:4], now[4:6], now[6:8], now[8:10], now[10:12], now[12:]
```

使用 slices 时是这样子的:

```
y, m, d, H, M, S = slices[:4, 4:6, 6:8, 8:10, 10:12, 12:](now)
```

而使用 cut 可以更简化:

```
y, m, d, H, M, S = cut(4, 6, 8, 10, 12)(now)
```

### decorator.cached_property

仅执行一次的 property。

