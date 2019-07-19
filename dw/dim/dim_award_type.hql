-- ******************************************************************************
-- 程序名称:     dim_award_type
-- 功能描述:     荣誉类型维度表
-- 输入参数:     无
-- 创建人名:     zonyee_lu
-- 创建日期:     20190719
-- ******************************************************************************

create table dim.dim_award_type(
type_id int comment 'id',
type_name string comment '类型'
) comment '荣誉类型维度表';

-- 初始化
insert into table dim.dim_data_type
select 0 as type_id, '最有价值球员MVP' as type_name union all
select 1 as type_id, '最佳新秀ROY' as type_name union all
select 2 as type_id, '最佳防守球员DPOY' as type_name union all
select 3 as type_id, '最佳第六人' as type_name union all
select 4 as type_id, '进步最快球员' as type_name union all
select 5 as type_id, '总决赛最有价值球员' as type_name union all
select 6 as type_id, '全明星最有价值球员' as type_name union all
select 17 as type_id, '最佳教练' as type_name;