# for single gpu
CUDA_VISIBLE_DEVICES=0 python train.py --cfg ./configs/pa100k.yaml

# for multi-gpu
#CUDA_VISIBLE_DEVICES=0,1 python -m torch.distributed.launch --nproc_per_node=2 --master_port=1233 train.py --cfg ./configs/pa100k.yaml
