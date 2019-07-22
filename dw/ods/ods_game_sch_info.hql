-- noinspection SqlDialectInspectionForFile

-- ******************************************************************************
-- 程序名称:     ods_game_sch_info.hql
-- 功能描述:     赛程信息表
-- 输入参数:     无
-- 创建人名:     zonyee_lu
-- 创建日期:     20190722
-- ******************************************************************************

create table ods.ods_game_sch_info(
play_date string comment '日期',
type string comment '类型',
game_id string comment '比赛id',
guest_team string comment '客队',
guest_team_poin string comment '客队得分',
home_team string comment '主队',
home_team_poin string comment '主队得分',
) comment '赛程信息表'
partitioned by (dt string);

load data local inpath " + txt_path + " overwrite into table ods.ods_game_sch_info partition(dt='${dt}');