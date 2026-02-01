from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# 20种水果数据
FRUITS = {
    '苹果': {
        'calories': 52,
        'vitamin_c': 4.6,
        'fiber': 2.4,
        'sugar': 10.4,
        'best_time': '上午10点或下午3点',
        'amount': '1-2个（中等大小）',
        'color': '#FF6B6B',
        'nutrition': ['维生素C', '膳食纤维', '钾', '抗氧化物质']
    },
    '香蕉': {
        'calories': 89,
        'vitamin_c': 8.7,
        'fiber': 2.6,
        'sugar': 12.2,
        'best_time': '早餐后或运动前后',
        'amount': '1-2根',
        'color': '#FFE66D',
        'nutrition': ['维生素B6', '钾', '纤维', '天然糖分']
    },
    '橙子': {
        'calories': 47,
        'vitamin_c': 53.2,
        'fiber': 2.4,
        'sugar': 9.4,
        'best_time': '早晨或下午茶',
        'amount': '1-2个',
        'color': '#FF9F43',
        'nutrition': ['维生素C', '叶酸', '钾', '类黄酮']
    },
    '葡萄': {
        'calories': 69,
        'vitamin_c': 3.2,
        'fiber': 0.9,
        'sugar': 16.3,
        'best_time': '下午3-4点',
        'amount': '15-20颗',
        'color': '#9B59B6',
        'nutrition': ['白藜芦醇', '花青素', '维生素C', '钾']
    },
    '草莓': {
        'calories': 32,
        'vitamin_c': 58.8,
        'fiber': 2.0,
        'sugar': 4.9,
        'best_time': '早餐搭配或下午茶',
        'amount': '8-10颗',
        'color': '#FF6B9D',
        'nutrition': ['维生素C', '锰', '叶酸', '抗氧化剂']
    },
    '蓝莓': {
        'calories': 57,
        'vitamin_c': 9.7,
        'fiber': 2.4,
        'sugar': 10.0,
        'best_time': '早餐或工作间隙',
        'amount': '1杯（约150克）',
        'color': '#5D9CEC',
        'nutrition': ['花青素', '维生素C', '维生素K', '锰']
    },
    '猕猴桃': {
        'calories': 61,
        'vitamin_c': 92.7,
        'fiber': 3.0,
        'sugar': 9.0,
        'best_time': '早餐或餐后',
        'amount': '1-2个',
        'color': '#8CC152',
        'nutrition': ['维生素C', '维生素K', '纤维', '叶酸']
    },
    '芒果': {
        'calories': 60,
        'vitamin_c': 36.4,
        'fiber': 1.6,
        'sugar': 13.7,
        'best_time': '午后或作为甜点',
        'amount': '1个（中等大小）',
        'color': '#FFAB40',
        'nutrition': ['维生素A', '维生素C', '纤维', '抗氧化物']
    },
    '梨': {
        'calories': 57,
        'vitamin_c': 4.3,
        'fiber': 3.1,
        'sugar': 9.8,
        'best_time': '餐后或下午',
        'amount': '1个',
        'color': '#48CFAD',
        'nutrition': ['纤维', '维生素C', '钾', '铜']
    },
    '桃子': {
        'calories': 39,
        'vitamin_c': 6.6,
        'fiber': 1.5,
        'sugar': 8.4,
        'best_time': '早餐或下午茶',
        'amount': '1-2个',
        'color': '#F8B195',
        'nutrition': ['维生素C', '维生素A', '纤维', '钾']
    },
    '樱桃': {
        'calories': 50,
        'vitamin_c': 7.0,
        'fiber': 1.6,
        'sugar': 8.0,
        'best_time': '下午或作为零食',
        'amount': '20-30颗',
        'color': '#E84393',
        'nutrition': ['花青素', '维生素C', '钾', '抗氧化物']
    },
    '西瓜': {
        'calories': 30,
        'vitamin_c': 8.1,
        'fiber': 0.4,
        'sugar': 6.2,
        'best_time': '夏季午后或运动后',
        'amount': '1-2片',
        'color': '#FF6B6B',
        'nutrition': ['水分', '维生素C', '维生素A', '钾']
    },
    '哈密瓜': {
        'calories': 34,
        'vitamin_c': 36.7,
        'fiber': 0.8,
        'sugar': 7.9,
        'best_time': '早晨或下午',
        'amount': '2-3片',
        'color': '#F4A261',
        'nutrition': ['维生素C', '维生素A', '钾', '叶酸']
    },
    '菠萝': {
        'calories': 50,
        'vitamin_c': 47.8,
        'fiber': 1.4,
        'sugar': 9.9,
        'best_time': '饭后（帮助消化）',
        'amount': '2-3块',
        'color': '#F39C12',
        'nutrition': ['维生素C', '锰', '溴化物', '纤维']
    },
    '柠檬': {
        'calories': 29,
        'vitamin_c': 53.0,
        'fiber': 2.8,
        'sugar': 2.5,
        'best_time': '早晨温水泡或调味用',
        'amount': '半个（泡水或调味）',
        'color': '#F1C40F',
        'nutrition': ['维生素C', '柠檬酸', '钾', '抗氧化物']
    },
    '石榴': {
        'calories': 83,
        'vitamin_c': 10.2,
        'fiber': 4.0,
        'sugar': 13.7,
        'best_time': '下午或作为健康零食',
        'amount': '1个中等大小',
        'color': '#C0392B',
        'nutrition': ['花青素', '维生素C', '纤维', '抗氧化物']
    },
    '山竹': {
        'calories': 73,
        'vitamin_c': 2.9,
        'fiber': 1.7,
        'sugar': 9.6,
        'best_time': '夏季午后',
        'amount': '2-3个',
        'color': '#5D4E37',
        'nutrition': ['膳食纤维', '维生素C', '维生素B', '矿物质']
    },
    '火龙果': {
        'calories': 60,
        'vitamin_c': 20.5,
        'fiber': 2.5,
        'sugar': 8.0,
        'best_time': '早餐或作为健康零食',
        'amount': '半个（中等大小）',
        'color': '#EC7063',
        'nutrition': ['维生素C', '纤维', '抗氧化物', '铁']
    },
    '椰子': {
        'calories': 354,
        'vitamin_c': 3.3,
        'fiber': 9.0,
        'sugar': 15.2,
        'best_time': '夏季或运动后补充能量',
        'amount': '适量（热量较高）',
        'color': '#95A5A6',
        'nutrition': ['健康脂肪', '纤维', '锰', '铜']
    },
    '荔枝': {
        'calories': 66,
        'vitamin_c': 71.5,
        'fiber': 1.3,
        'sugar': 15.2,
        'best_time': '夏季午后（不宜空腹）',
        'amount': '10-15颗',
        'color': '#E74C3C',
        'nutrition': ['维生素C', '钾', '纤维', '抗氧化物']
    }
}

@app.route('/')
def index():
    return render_template('index.html', fruits=FRUITS)

@app.route('/draw')
def draw():
    # 随机抽选水果
    fruit_name = random.choice(list(FRUITS.keys()))
    fruit_data = FRUITS[fruit_name]
    return jsonify({
        'name': fruit_name,
        'data': fruit_data
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)
