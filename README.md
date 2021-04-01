# LanguageTransfer

## Negative language transfer dataset
To access the negative language transfer annotations added to the errors made by Chinese native speakers whose essays are part of the FCE dataset, you need to have downloaded the FCE dataset from <a href="https://www.ilexir.co.uk/datasets/index.html" target="_blank">https://www.ilexir.co.uk/datasets/index.html</a>.

After downloading, and as consequence signing the FCE dataset's license agreement, fill and submit <a href="https://forms.gle/aW746U9CNuPqqWL2A" target="_blank">this form</a>.
Once the form is submitted you will be granted access to the negative language transfer annotated errors dataset.

### Data format
The negative language transfer annotated data follows the format described in the [data_description.md](data_description.md) file.

### Citation
When using the negative language transfer annotated data, you are encouraged to cite the following papers:

```
@inproceedings{nlt-dataset,
    title = "Negative language transfer in learner {E}nglish: {A} new dataset",
    author = "Wanderley, Leticia Farias  and
      Zhao, Nicole  and
      Demmans Epp, Carrie",
    booktitle="Proceedings of the 2021 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies",
    year = "2021",
    publisher = "In press"
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

## Negative language transfer classification
To view the code used to analyse the predictive power of logistic regression and random forest models in classifying learner errors as negative language transfer, go to the <a href="https://github.com/leticiawanderley/nlt-classification/" target="_blank">nlt-classification</a> folder.
