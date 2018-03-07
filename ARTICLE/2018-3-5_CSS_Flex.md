
# Flex
## Container
| Container prop  | 具体含义 | value                                                         |
|:----------------|:---------|:--------------------------------------------------------------|
| flex-direction  | 主轴方向 | row\row-reverse\column\column-reverse                         |
| flex-wrap       | 如何换行 | nowrap\wrap\wrap-reverse                                      |
| flex-flow       | 上二简写 | \<flex-direction> \<flex-wrap>                                |
| justify-content | 主轴对齐 | flex-start\flex-end\center\space-between\space-around         |
| align-items     | 叉轴对齐 | flex-start\flex-end\center\baseline\stretch                   |
| align-content   | 多轴对齐 | flex-start\flex-end\center\space-between\space-around\stretch |

## Item

| Item prop   | 具体含义         | value                                               |
|:------------|:-----------------|:----------------------------------------------------|
| order       | 项目主轴排列顺序 | /* default 0 */                                     |
| flex-grow   | 有空余时放大比例 | /* default 1 */                                     |
| flex-shrink | 有不足时收缩比例 | /* default 1 */                                     |
| flex-basis  | 项目单元本身大小 | /* default auto */                                  |
| flex        | 上面三者合并简写 | [ \<'flex-grow'> \<'flex-shrink'> \<'flex-basis'> ] |
| align-self  | 单独设定叉轴对齐 | auto\flex-start\flex-end\center\baseline\stretch    |


