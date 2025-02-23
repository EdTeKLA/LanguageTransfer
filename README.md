# LanguageTransfer

## Negative language transfer dataset (Chinese speakers)
To access the negative language transfer annotations added to the errors made by Chinese native speakers whose essays are part of the FCE dataset, you need to have downloaded the FCE dataset from <a href="https://www.ilexir.co.uk/datasets/index.html" target="_blank">https://www.ilexir.co.uk/datasets/index.html</a>.

After downloading, and as consequence signing the FCE dataset's license agreement, fill and submit <a href="https://forms.gle/gKXwCDP5SGsswkut5" target="_blank">this form</a>.
Once the form is submitted you will be granted access to the negative language transfer annotated errors dataset.

### Data format
The negative language transfer annotated data follows the format described in the [data_description.md](data_description.md) file.

### Citation
When using the negative language transfer annotated data, you are encouraged to cite the following papers:

```
@inproceedings{farias-wanderley-etal-2021-negative,
    title = "Negative language transfer in learner {E}nglish: A new dataset",
    author = "Farias Wanderley, Leticia  and
      Zhao, Nicole  and
      Demmans Epp, Carrie",
    booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2021.naacl-main.251",
    pages = "3129--3142"
}

@inproceedings{yannakoudakis2011fce,
 title={A new dataset and method for automatically grading ESOL texts},
 author={Yannakoudakis, Helen and Briscoe, Ted and Medlock, Ben},
 booktitle={Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies-Volume 1},
 pages={180--189},
 year={2011},
 organization={Association for Computational Linguistics}
}
```

## Negative language transfer dataset (Farsi speakers)
To access the negative language transfer annotations added to the errors made by Farsi native speakers whose essays are part of the Lang-8 dataset, fill and submit <a href="https://docs.google.com/forms/d/e/1FAIpQLSccWWkP_6kzUJSekgPUx4IFLWq29J8fmeuqaJTQyN-dTpbXGQ/viewform?usp=sharing" target="_blank">this form</a>.

## Negative language transfer classification
To view the code used to analyse the predictive power of logistic regression and random forest models in classifying learner errors as negative language transfer, go to the <a href="https://github.com/leticiawanderley/nlt-classification/" target="_blank">nlt-classification</a> repository.

## Identifying negative language transfer in learner errors using POS information
In this work, learner errors were converted into part-of-speech (POS) tag sequences and analysed by language models that represented POS tag sequences found in the first and second languages. To learn more about using POS tag sequences to detect negative language transfer, follow this link to the <a href="https://github.com/leticiawanderley/identifying-nlt/" target="_blank">identifying-nlt</a> repository.
