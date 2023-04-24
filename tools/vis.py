import numpy as np


def tb_visualizer_pedes(tb_writer, lr, epoch, train_loss, valid_loss, train_result, valid_result,
                        train_gt, valid_gt, train_loss_mtr, valid_loss_mtr, model, attr_name):
    # tb_writer.add_scalars('lr', {'lr': lr}, epoch)
    # tb_writer.add_scalars('losses', {'train': train_loss,
    #                                      'test': valid_loss}, epoch)
    #
    # tb_writer.add_scalars('train_perf/ma', {'ma': train_result.ma,
    #                                      'pos_recall': np.mean(train_result.label_pos_recall),
    #                                      'neg_recall': np.mean(train_result.label_neg_recall),
    #                                      'Acc': train_result.instance_acc,
    #                                      'Prec': train_result.instance_prec,
    #                                      'Rec': train_result.instance_recall,
    #                                      'F1': train_result.instance_f1}, epoch)
    #
    # tb_writer.add_scalars('test_perf/', {'ma': valid_result.ma,
    #                                     'pos_recall': np.mean(valid_result.label_pos_recall),
    #                                     'neg_recall': np.mean(valid_result.label_neg_recall),
    #                                     'Acc': valid_result.instance_acc,
    #                                     'Prec': valid_result.instance_prec,
    #                                     'Rec': valid_result.instance_recall,
    #                                     'F1': valid_result.instance_f1}, epoch)

    tb_writer.add_scalar('lr/epoch', lr, epoch)
    tb_writer.add_scalar('losses/train', train_loss, epoch)
    tb_writer.add_scalar('losses/test', valid_loss, epoch)

    tb_writer.add_scalar('train_perf/ma', train_result.ma, epoch)
    tb_writer.add_scalar('train_perf/pos_recall', np.mean(train_result.label_pos_recall), epoch)
    tb_writer.add_scalar('train_perf/neg_recall', np.mean(train_result.label_neg_recall), epoch)
    tb_writer.add_scalar('train_perf/Acc', train_result.instance_acc, epoch)
    tb_writer.add_scalar('train_perf/Prec', train_result.instance_prec, epoch)
    tb_writer.add_scalar('train_perf/Rec', train_result.instance_recall, epoch)
    tb_writer.add_scalar('train_perf/F1', train_result.instance_f1, epoch)

    tb_writer.add_scalar('test_perf/ma', valid_result.ma, epoch)
    tb_writer.add_scalar('test_perf/pos_recall', np.mean(valid_result.label_pos_recall), epoch)
    tb_writer.add_scalar('test_perf/neg_recall', np.mean(valid_result.label_neg_recall), epoch)
    tb_writer.add_scalar('test_perf/Acc', valid_result.instance_acc, epoch)
    tb_writer.add_scalar('test_perf/Prec', valid_result.instance_prec, epoch)
    tb_writer.add_scalar('test_perf/Rec', valid_result.instance_recall, epoch)
    tb_writer.add_scalar('test_perf/F1', valid_result.instance_f1, epoch)


