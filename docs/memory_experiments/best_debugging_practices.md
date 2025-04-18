
# Best Debugging Practices for Text-to-SQL Agentic Pipeline

## Common Issues and Solutions

### 1. Logical Errors in Syntactically Valid SQL
- **Issue**: SQL can pass syntax validation but produce incorrect results  
- **Solution**: Enhance your glossary with semantic relationships and domain-specific examples  
- **Example**: When querying for "best selling products," the model might sort by revenue instead of units sold  
- **Action**: Add explicit definitions in your glossary:  
  `"best_selling": "Refers to products with highest unit sales, not revenue"`

### 2. Model Selection Strategy

- **Primary Model**: Use robust models for initial query generation (e.g., Llama 3.1-8B)

- **Specialized Models**: Use dedicated models for tasks that need focused capabilities:
    - **Data generation**: Models with strong pattern recognition
    - **Debugging**: Models with good reasoning abilities
    - **Fine-tuning**: Balance between performance and training efficiency

- **Practical Approach**: Keep a baseline model for general use, but experiment with specialized models in components where errors persist

### 3. Case Sensitivity and String Normalization
- **Issue**: Models may struggle with case differences (`"lamini"` vs. `"Lamini"`)
- **Solution**: Provide examples in your glossary showing variations  
- **Example Glossary Entry**:
  ```json
  "brands": {
    "definition": "Product manufacturers",
    "examples": ["Lamini", "LlamaCo", "Sheep Inc."],
    "case_sensitivity": "Brand names are case-sensitive in our database"
  }
  ```

### 4. Business Logic Representation
- **Issue**: Models struggle with domain-specific calculations  
- **Solution**: Include formulas and calculation methods in your glossary  
- **Example**:
  ```json
  "sales_volume": {
    "definition": "Total units sold in a time period",
    "calculation": "SUM(units_sold) WHERE date BETWEEN start_date AND end_date",
    "examples": [
      {
        "question": "What was the sales volume in January?", 
        "sql": "SELECT SUM(units_sold) FROM sales WHERE date BETWEEN '2025-01-01' AND '2025-01-31'"
      }
    ]
  }
  ```

### 5. Preventing Overfitting
- **Generate Diverse Training Data**: Use multiple question generators to create varied examples  
- **Verify Coverage**: Analyze generated data to ensure all SQL concepts are represented  
- **Testing Approach**: Reserve truly novel questions for evaluation that weren't in training  

---

## Understanding SQL Validation Limitations

### Lamini's `SQLValidator` Capabilities and Gaps

The `SQLValidator` uses `EXPLAIN QUERY PLAN` for basic validation:

- ✅ **Catches**:
    - Syntax errors
    - Missing tables or columns

- ❌ **Misses**:
    - Runtime errors
    - Logical flaws (e.g., wrong WHERE clause logic)
    - Data type mismatches
    - SQL dialect incompatibilities

**Examples of what it can’t catch:**
- Data type mismatches:
  ```sql
  SELECT * FROM users WHERE age = 'abc';
  ```
- Invalid operations:
  ```sql
  SELECT total_amount / 0 FROM sales;
  ```
- Unsupported functions:
  ```sql
  SELECT DATEADD(day, 5, '2024-01-01');  -- Fails in SQLite
  ```

---

## Enhanced Validation Approaches

### 1. Runtime Execution Validator
- **Pros**: Catches actual execution errors
- **Cons**: May timeout on large datasets or inefficient queries
- **Implementation**: Add timeout thresholds and sandbox execution

### 2. Result Validation Checker
- **Limitation**: Empty results may be valid (e.g., no matching records)
- **Solution**: Validate sample queries with known results

---

## Systematic Error Resolution

### Common Error Categories and Fixes

#### 1. Missing Object Errors
- **Issue**: Queries fail due to column or table names that don't exist  
- **Fix**: Implement fuzzy matching
  ```python
  # "customer_nme" doesn't exist, but suggest closest match
  suggested_column = find_similar_column("customer_nme", schema_columns)
  ```

#### 2. Data Format Inconsistencies
- **Issue**: Format differences cause mismatches  
- **Fix**: Provide example values in glossary  
  ```json
  "location": {
    "definition": "Customer location",
    "format": "City, State",
    "examples": ["Sacramento, CA", "Boston, MA"]
  }
  ```

#### 3. SQL Dialect Differences
- **Issue**: Functions vary across SQL dialects  
- **Fix**: Maintain function mapping table  
  ```json
  "function_mappings": {
    "DATEADD": {
      "sqlite": "datetime(date, '+N days')",
      "postgres": "date + interval 'N days'"
    }
  }
  ```

---
