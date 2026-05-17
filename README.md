# Macro Regime Experiment v2

一个可直接放到 GitHub 运行的宏观 regime 监控工具。

它会抓取 FRED 和 Yahoo Finance 数据，生成：

- `reports/latest.md`：人类可读的宏观状态报告；
- `data/latest.json`：完整机器可读输出；
- `data/history.csv`：每次运行后的历史记录。

## 核心升级

v2 不再只依赖规则评分 + 固定 Markov prior，而是加入了两个稳健统计层：

1. **Student-t observation filter + Markov transition smoothing**
   - 使用规则生成的历史伪标签估计每个 regime 的稳健观测分布；
   - 用 Student-t 对厚尾金融数据更稳健；
   - 用 Markov transition 做状态平滑，但不把它当作唯一统计引擎。

2. **Robust change-point / transition-risk score**
   - 用 trailing-window 的稳健 z-score 距离识别异常变化；
   - 对 R1 → R2 的突变风险更敏感；
   - 同时结合信用、美元、权益、小盘、新兴市场、长久期债券的 stress votes。

最终输出为 ensemble probability：

```text
rule posterior + Student-t filter probability + change-point transition risk
```

## Regime 定义

| Regime | Name | 中文解释 | 核心特征 |
|---|---|---|---|
| R0 | High-rate absorption | 高利率吸收 | 利率高但不再加速，权益有韧性，信用稳定 |
| R1 | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 | 长端利率上行、美元走强、小盘和 EM 承压，信用尚未失序 |
| R2 | Credit / sovereign stress spillover | 信用 / 主权压力外溢 | 信用利差扩张、HYG 下跌、风险资产同步去杠杆 |
| R3 | Rate decline / policy repair | 利率下行 / 政策修复 | 利率下行、TLT 上涨、信用稳定、风险资产修复 |

## 本地运行

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m unittest discover -s tests -p 'test_*.py'
python runner.py \
  --previous-regime auto \
  --output reports/latest.md \
  --json-output data/latest.json \
  --history-csv data/history.csv \
  --start 2020-01-01 \
  --period 5y
```

## GitHub Actions 运行

1. 新建或打开 GitHub repo。
2. 上传本 ZIP 解压后的全部文件，保留 `.github/workflows/macro-regime.yml` 路径。
3. 打开 repo 的 **Actions** tab。
4. 选择 **Macro Regime Daily Update v2**。
5. 点击 **Run workflow** 手动测试一次。
6. 之后工作流会在周一至周五 `23:30 UTC` 自动运行。

## 输出解释

### `reports/latest.md`

包含：

- 数据时间戳与新鲜度；
- 当前最可能 regime；
- 证据表；
- ensemble probability；
- rule posterior；
- Student-t filter probability；
- change-point / transition-risk score；
- risk alerts；
- 下一步观察指标。

### `data/latest.json`

完整结构化输出，适合后续可视化、回测或告警系统读取。

### `data/history.csv`

每次运行追加一行，用于后续 walk-forward validation、Brier score、calibration curve 和 regime transition 分析。

## 重要限制

- 这是宏观状态监控工具，不是自动交易系统。
- 当前 Student-t filter 使用规则伪标签估计观测分布，不等于已经人工标注、样本外验证的完整 HMM。
- 输出概率是“模型内部权重”，只有经过历史标签与样本外校准后，才能被解释为严格统计概率。
- R2 不应只因利率上行或股票下跌触发；需要信用利差、主权利差或多资产同步去杠杆确认。

## 建议后续增强

1. 接入 VIX、MOVE、CCC OAS、CDX、OAT/Bund、BTP/Bund、SOFR-OIS 等压力指标。
2. 建立人工 regime 标签，做 walk-forward validation。
3. 对概率做 Brier score、log loss、reliability curve、isotonic calibration。
4. 若数据量足够，再升级为完整 Hidden Semi-Markov Model，用于建模 regime duration。
