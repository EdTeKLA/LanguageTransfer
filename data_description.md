## Data description

Each line in this dataset represents an annotated learner error.
One paragraph line in the essay XML file can contain more than one annotated error.

| Column        | Type   | Description  |
| ------------- |:------:|-------------|
| student_id    | String | Test taker identification |
| language      | String | Learner's L1    |
| overall_score | Float | Combined mark for both tasks     |
| exam_score    | String | Essay mark |
| raw_sentence  | String | Paragraph line extracted from the XML file      |
| error_type    | String | Tag associated with the error (See [Nicholls (2003)](http://ucrel.lancs.ac.uk/publications/CL2003/papers/nicholls.pdf))    |
| error_length    | Integer | How many words are tagged in the error |
| correction_length      | Integer | How many words are tagged in the correction      |
| correct_sentence    | String | Sentence with all the errors replaced by their corrections |
| correct_error_index | Integer | Index of the correction in the sentence     |
| incorrect_sentence | String | Sentence with all the errors replaced by their corrections, **but the error represented by the row**      |
| incorrect_error_index      | Integer | Index of the error in the sentence        |