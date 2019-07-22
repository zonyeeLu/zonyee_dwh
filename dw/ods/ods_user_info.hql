-- noinspection SqlDialectInspectionForFile

-- ******************************************************************************
-- 程序名称:     ods_player_info.hql
-- 功能描述:     球员教练信息表
-- 输入参数:     无
-- 创建人名:     zonyee_lu
-- 创建日期:     20190721
-- ******************************************************************************

create table ods.ods_player_info(
player_name string comment '名称',
player_id string comment 'id',
player_tpye string comment '类型'
) comment '球员教练信息表';

load data local inpath " + txt_path + " overwrite into table ods.ods_player_info partition(dt='${dt}');