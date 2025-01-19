# Customer Feedback Analysis

## Problem Statement
Capital One's marketing team is working on a project to analyze customer feedback from their feedback surveys. 

The team sorted the words from the feedback into three different categories:
- short_comments
- mid_length_comments
- long_comments

The team wants to find comments that are not short and that come from social media. The output should include:
- `feedback_id`
- `feedback_text`
- `source_channel`
- `comment_category`

### Table
- **customer_feedback**:
  - `feedback_id` (bigint): Unique ID for each feedback.
  - `feedback_text` (text): Text of the feedback provided by customers.
  - `source_channel` (text): Source where the feedback was collected (e.g., social media, email, survey).
  - `comment_category` (text): Category of the comment (e.g., short_comments, mid_length_comments, long_comments).

---

## SQL Solution

```sql
SELECT 
    feedback_id,
    feedback_text,
    source_channel,
    comment_category
FROM 
    customer_feedback
WHERE 
    comment_category NOT LIKE 'short_comments' 
    AND
    source_channel LIKE 'social_media';
```

---

## Explanation

### Query Logic
1. **Select Relevant Columns**:
   - The query retrieves the columns `feedback_id`, `feedback_text`, `source_channel`, and `comment_category` from the `customer_feedback` table.

2. **Filter Conditions**:
   - `comment_category NOT LIKE 'short_comments'`: Ensures the results exclude feedback categorized as "short_comments."
   - `source_channel LIKE 'social_media'`: Ensures the feedback is collected from the "social_media" source channel.

### Combined Filters
- The `WHERE` clause combines the conditions using `AND` to ensure only feedback that is not short and comes from social media is included.

---

## Example Input and Output

### Input Data
#### Table: customer_feedback
| feedback_id | feedback_text                                                | source_channel | comment_category   |
|-------------|-------------------------------------------------------------|----------------|--------------------|
| 9           | Had some issues with billing, but they were resolved quickly. | social_media   | mid_length_comments|
| 15          | Terrible experience, the app crashes all the time.           | social_media   | mid_length_comments|
| 20          | Navigating the website was challenging, and the customer support response time was slower than expected. Improvements in these areas would greatly enhance the user experience. | social_media   | long_comments      |
| 11          | Excellent service and prompt response.                       | social_media   | short_comments     |

### Output Data
| feedback_id | feedback_text                                                | source_channel | comment_category   |
|-------------|-------------------------------------------------------------|----------------|--------------------|
| 9           | Had some issues with billing, but they were resolved quickly. | social_media   | mid_length_comments|
| 15          | Terrible experience, the app crashes all the time.           | social_media   | mid_length_comments|
| 20          | Navigating the website was challenging, and the customer support response time was slower than expected. Improvements in these areas would greatly enhance the user experience. | social_media   | long_comments      |

---

## Conclusion
This query efficiently filters out short comments and focuses only on feedback from social media. It provides insights into customer opinions that are more substantial and sourced from social channels, which is valuable for targeted analysis by the marketing team.
