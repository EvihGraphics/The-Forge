# AVBOIT Debug View Mapping

Source: `Examples_3/Unit_Tests/src/15_Transparency/15_Transparency.cpp`

| ID | UI Name | P2.6R interpretation |
| --- | --- | --- |
| 0 | Final | Final resolved AVBOIT output. |
| 1 | Low-resolution total transmittance | Upsampled low-resolution total transmittance diagnostic. |
| 2 | Full-resolution transparent coverage | Coverage from actual full-resolution transparent fragments. |
| 3 | Full-resolution accumulated extinction | Full-resolution accumulated extinction diagnostic. |
| 4 | Full-resolution normalization denominator | Full-resolution normalization denominator diagnostic. |
| 5 | Final resolve opacity | Final resolve opacity diagnostic. |
| 6 | AVBOIT z slice | Voxel z slice diagnostic. |
| 7 | AVBOIT legacy weight | Current-run weight proxy for legacy mode. It is not a simultaneous legacy/front diff image. |
| 8 | AVBOIT candidate front weight | Current-run weight proxy for front mode. It is not a simultaneous legacy/front diff image. |
| 9 | AVBOIT denominator | AVBOIT denominator diagnostic. |
| 10 | AVBOIT opacity | AVBOIT opacity diagnostic. |
| 11 | AVBOIT opacity denominator ratio | Opacity/denominator ratio diagnostic. |
| 12 | AVBOIT weighted color sum | Weighted color sum diagnostic. |
| 13 | AVBOIT front minus legacy weight | Current-run direction proxy. True legacy/front difference is measured by paired captures. |
| 14 | AVBOIT analytic error proxy | Analytic error proxy diagnostic. |

P2.6R conclusion: debug views `7` and `8` change when `--avboit-transmittance-direction` changes, but final view `0` remains byte-identical for all paired legacy/front analytic captures in this result set.
