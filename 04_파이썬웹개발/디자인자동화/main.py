from typing import Dict, Any
import os
import requests
from faker import Faker
import random
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# Faker 설정 (한국어)
fake = Faker('ko_KR')

# Figma 파일 정보
FILE_KEY = "WrUpT7OHq8QBU1YCfpsjJJ"

# 각 상품 컴포넌트의 노드 ID 형식
PRODUCT_NODE_IDS = {
    "name": "1:6424",      # 상품명 텍스트 레이어의 베이스 ID
    "price": "1:6425",     # 가격 텍스트 레이어의 베이스 ID
    "description": "1:6426", # 설명 텍스트 레이어의 베이스 ID
    "rating": "1:6427",    # 평점 텍스트 레이어의 베이스 ID
    "reviews": "1:6428"    # 리뷰 수 텍스트 레이어의 베이스 ID
}

def generate_random_product() -> Dict[str, Any]:
    """랜덤 상품 정보 생성"""
    return {
        "name": fake.word() + " " + fake.word(),
        "price": f"₩{random.randint(10000, 1000000):,}",
        "description": fake.sentence(),
        "rating": f"{random.uniform(3.0, 5.0):.1f}",
        "reviews": str(random.randint(10, 1000))
    }

def main():
    # Figma 토큰은 환경변수에서 가져옵니다
    figma_token = os.getenv("FIGMA_ACCESS_TOKEN")
    if not figma_token:
        print("Error: FIGMA_ACCESS_TOKEN이 설정되지 않았습니다.")
        return

    # Figma API 헤더 설정
    headers = {
        "X-Figma-Token": figma_token,
        "Content-Type": "application/json"
    }

    try:
        # 파일 데이터 가져오기
        print("Figma 파일 데이터를 가져오는 중...")
        response = requests.get(
            f"https://api.figma.com/v1/files/{FILE_KEY}",
            headers=headers
        )
        response.raise_for_status()
        
        # 상품 데이터 생성
        print("랜덤 상품 데이터 생성 중...")
        products = [generate_random_product() for _ in range(9)]  # 9개 상품 생성
        
        # 파일의 모든 텍스트 노드 가져오기
        print("텍스트 노드 정보 가져오는 중...")
        nodes_response = requests.get(
            f"https://api.figma.com/v1/files/{FILE_KEY}",
            headers=headers
        )
        nodes_response.raise_for_status()
        file_data = nodes_response.json()

        # 각 상품에 대한 업데이트 수행
        print("Figma 디자인 업데이트 중...")
        for i, product in enumerate(products):
            # 텍스트 노드 ID 찾기 (프레임 내의 텍스트 노드)
            node_id = f"{i+1}:{PRODUCT_NODE_IDS['name']}"  # 예상되는 노드 ID 형식
            
            # 텍스트 업데이트를 위한 데이터 준비
            updates = {
                "requests": [
                    {
                        "type": "TEXT",
                        "nodeId": node_id,
                        "characters": product["name"]
                    },
                    {
                        "type": "TEXT",
                        "nodeId": f"{i+1}:{PRODUCT_NODE_IDS['price']}",
                        "characters": product["price"]
                    },
                    {
                        "type": "TEXT",
                        "nodeId": f"{i+1}:{PRODUCT_NODE_IDS['description']}",
                        "characters": product["description"]
                    },
                    {
                        "type": "TEXT",
                        "nodeId": f"{i+1}:{PRODUCT_NODE_IDS['rating']}",
                        "characters": product["rating"]
                    },
                    {
                        "type": "TEXT",
                        "nodeId": f"{i+1}:{PRODUCT_NODE_IDS['reviews']}",
                        "characters": f"({product['reviews']})"
                    }
                ]
            }
            
            try:
                # 텍스트 업데이트 요청
                response = requests.put(
                    f"https://api.figma.com/v1/files/{FILE_KEY}",
                    headers=headers,
                    json=updates
                )
                response.raise_for_status()
                print(f"상품 {i+1} 업데이트 완료")
            except Exception as e:
                print(f"Warning: 상품 {i+1} 업데이트 실패: {e}")
            except Exception as e:
                print(f"Warning: 상품 {i+1} 업데이트 실패: {e}")
        
        print("디자인 업데이트가 완료되었습니다!")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
