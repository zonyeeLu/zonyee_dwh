-- ******************************************************************************
-- 程序名称:     dim_data_type
-- 功能描述:     数据范围维度表
-- 输入参数:     无
-- 创建人名:     zonyee_lu
-- 创建日期:     20190715
-- ******************************************************************************

create table dim.dim_data_type(
type_name string comment '数据范围缩写',
type_cn_name string comment '数据范围中文'
) comment '数据范围维度表';

-- 初始化
insert into table dim.dim_data_type
select 'all' as type_name, '全场' as type_cn_name union all
select '1h' as type_name, '上半场' as type_cn_name union all
select '2h' as type_name, '下半场' as type_cn_name union all
select '1q' as type_name, '第一节' as type_cn_name union all
select '2q' as type_name, '第二节' as type_cn_name union all
select '3q' as type_name, '第三节' as type_cn_name union all
select '4q' as type_name, '第四节' as type_cn_name union all
select '5l' as type_name, '最后五分钟' as type_cn_name union all
select '2l' as type_name, '最后120秒' as type_cn_name;