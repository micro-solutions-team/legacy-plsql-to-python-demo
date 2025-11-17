/* 
 Legacy eligibility rules implemented in PL/SQL.
 Rules have been modified multiple times over the years.
*/

PROCEDURE evaluate_eligibility (
    p_customer_id    IN NUMBER,
    p_customer_type  IN VARCHAR2,
    p_monthly_usage  IN NUMBER,
    p_debt_amount    IN NUMBER,
    o_eligible       OUT VARCHAR2
) IS
BEGIN
    o_eligible := 'Y';

    IF p_monthly_usage > 600 THEN
        o_eligible := 'N';
    END IF;

    IF p_customer_type = 'VIP' THEN
        o_eligible := 'Y';
    END IF;

    IF p_debt_amount > 1000 THEN
        o_eligible := 'N';
    END IF;
END;
