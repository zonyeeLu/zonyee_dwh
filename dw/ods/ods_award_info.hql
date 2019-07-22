-- noinspection SqlDialectInspectionForFile
-- ******************************************************************************
-- 程序名称:     ods_award_info.hql
-- 功能描述:     荣誉表
-- 输入参数:     无
-- 创建人名:     zonyee_lu
-- 创建日期:     20190722
-- ******************************************************************************

create table ods.ods_player_info(
season string comment '赛季',
player_name string comment '球员名称',
player_type string comment '球员类型',
player_id string comment '球员id',
league string comment '联盟',
play_times string comment '出场次数',
start_times string comment '首发次数',
play_time string comment '场均时间',
shot_rate string comment '投篮命中率',
get_nums string comment '投篮命中数',
shot_nums string comment '场均出手次数',
three_rate string comment '三分命中率',
three_get_nums string comment '场均三分命中个数',
three_nums string comment '场均三分出手次数',
free_rate string comment '罚球命中率',
free_get_nums string comment '场均罚球命中数',
free_nums string comment '场均罚球出手次数',
reb_nums string comment '场均篮板球',
off_reb_nums string comment '场均前场篮板',
def_reb_nums string comment '场均后场篮板',
assi_nums string comment '场均助攻',
stl_nums string comment '场均抢断',
blk_nums string comment '场均盖帽',
trunover_nums string comment '场均失误',
foul_times string comment '场均犯规',
point string comment '场均得分',
) comment '荣誉表'
partitioned by (dt string);

load data local inpath " + txt_path + " overwrite into table ods.ods_player_info partition(dt='${dt}');