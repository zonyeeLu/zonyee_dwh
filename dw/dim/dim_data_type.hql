-- ******************************************************************************
-- 程序名称:     dim_data_type
-- 功能描述:     数据类型维度表
-- 输入参数:     无
-- 创建人名:     zonyee_lu
-- 创建日期:     20190715
-- ******************************************************************************

create table dim.dim_data_type(
type_name string comment '数据类型缩写',
type_cn_name string comment '数据类型中文'
) comment '数据类型维度表';

-- 初始化
insert into table dim.dim_data_type
select 'pts' as type_name, '得分榜' as type_cn_name union all
select 'trb' as type_name, '篮板榜' as type_cn_name union all
select 'ast' as type_name, '助攻榜' as type_cn_name union all
select 'blk' as type_name, '盖帽榜' as type_cn_name union all
select 'stl' as type_name, '抢断榜' as type_cn_name union all
select 'tov' as type_name, '失误榜' as type_cn_name union all
select 'pf' as type_name, '犯规榜' as type_cn_name union all
select 'ts' as type_name, '真实命中率榜' as type_cn_name union all
select 'fg' as type_name, '命中榜' as type_cn_name union all
select 'fgper' as type_name, '投篮命中率榜' as type_cn_name union all
select 'threep' as type_name, '三分榜' as type_cn_name union all
select 'threepper' as type_name, '三分命中率榜' as type_cn_name union all
select 'ft' as type_name, '罚球榜' as type_cn_name union all
select 'ftper' as type_name, '罚球命中率榜' as type_cn_name union all
select 'g' as type_name, '出场次数榜' as type_cn_name union all
select 'kobe'  as type_name, '打铁' as type_cn_name union all
select 'per'  as type_name, '效率值榜' as type_cn_name