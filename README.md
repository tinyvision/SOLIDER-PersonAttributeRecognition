# SOLIDER on [Person Attribute Recognition]

This repo provides details about how to use [SOLIDER](https://github.com/tinyvision/SOLIDER) pretrained representation on attribute recognition task.
We modify the code from [Rethinking_of_PAR](https://github.com/valencebond/Rethinking_of_PAR), and you can refer to the original repo for more details.

## Installation and Datasets

Details of installation and dataset preparation can be found in [Rethinking_of_PAR](https://github.com/valencebond/Rethinking_of_PAR).

## Prepare Pre-trained Models
Step 1. Download models from [SOLIDER](https://github.com/tinyvision/SOLIDER), or use [SOLIDER](https://github.com/tinyvision/SOLIDER) to train your own models.

Steo 2. Put the pretrained models under the `pretrained` file, and rename their names as `./pretrained/solider_swin_tiny(small/base).pth`

## Training
Train with single GPU or multiple GPUs:

```shell
sh run.sh
```

## Performance

| Method | Model | PETA_ZS<br>(mA) | RAP_ZS<br>(mA) | PA100K<br>(mA) |
| ------ | :---: | :---: | :---: | :---: |
| SOLIDER | Swin Tiny | 74.37 | 74.23 | 84.14 |
| SOLIDER | Swin Small | 76.21 | 75.95 | 86.25 |
| SOLIDER | Swin Base | 76.43 | 76.42 | 86.37 |

- We use the pretrained models from [SOLIDER](https://github.com/tinyvision/SOLIDER).
- The semantic weight is set to 0.8 in these experiments.

## Citation

If you find this code useful for your research, please cite our paper

```
@inproceedings{chen2023beyond,
  title={Beyond Appearance: a Semantic Controllable Self-Supervised Learning Framework for Human-Centric Visual Tasks},
  author={Weihua Chen and Xianzhe Xu and Jian Jia and Hao Luo and Yaohua Wang and Fan Wang and Rong Jin and Xiuyu Sun},
  booktitle={The IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year={2023},
}
```
