-- 1. Top 5 fund houses by AUM
SELECT fund_house, SUM(aum_crore) AS total_aum_crore
FROM "03_aum_by_fund_house"
GROUP BY fund_house
ORDER BY total_aum_crore DESC
LIMIT 5;

-- 2. Average NAV per month
SELECT 
    amfi_code,
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS avg_nav
FROM "02_nav_history"
GROUP BY amfi_code, month
ORDER BY amfi_code, month;

-- 3. SIP YoY growth
SELECT 
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS total_sip_amount
FROM "08_investor_transactions"
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;

-- 4. Transactions by state
SELECT state, COUNT(*) AS total_transactions
FROM "08_investor_transactions"
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with expense ratio < 1%
SELECT scheme_name, fund_house, expense_ratio_pct
FROM "01_fund_master"
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- 6. Top 5 schemes by AUM
SELECT scheme_name, fund_house, aum_crore
FROM "07_scheme_performance"
ORDER BY aum_crore DESC
LIMIT 5;

-- 7. Average returns by category
SELECT category, AVG(return_3yr_pct) AS avg_3yr_return
FROM "07_scheme_performance"
GROUP BY category
ORDER BY avg_3yr_return DESC;

-- 8. Risk grade-wise fund count
SELECT risk_grade, COUNT(*) AS total_funds
FROM "07_scheme_performance"
GROUP BY risk_grade;

-- 9. KYC status distribution
SELECT kyc_status, COUNT(*) AS total_records
FROM "08_investor_transactions"
GROUP BY kyc_status;

-- 10. Average transaction amount by transaction type
SELECT transaction_type, AVG(amount_inr) AS avg_transaction_amount
FROM "08_investor_transactions"
GROUP BY transaction_type;