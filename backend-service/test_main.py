from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}


def wrong_stock():
    response = client.get("/api/bars?stock=AAPLl")
    assert response.status_code == 200
    assert response.json() == {"AAPLl": []}


def correct_stock():
    response = client.get("/api/news?stocks=FB")
    assert response.status_code == 200
    assert response.json() == {"news": [
        {
            "author": "Benzinga Insights",
            "content": "",
            "created_at": "2022-06-09T18:08:19Z",
            "headline": "Virtual Land Just Sold For 17,888 MANA In Decentraland",
            "id": 27632130,
            "images": [
                {
                    "size": "large",
                    "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/images/story/2022/decentraland_nft_image_176.png"
                },
                {
                    "size": "small",
                    "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/images/story/2022/decentraland_nft_image_176.png"
                },
                {
                    "size": "thumb",
                    "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/images/story/2022/decentraland_nft_image_176.png"
                }
            ],
            "source": "benzinga",
            "summary": "What happened: Virtual land tokenized as an NFT just sold for $17,682, which is 4.47x the current floor price of 2.2 Ethereum (CRYPTO: ETH) ($17,682 USD). The collection consists of over 97,000 plots of land –– at the current moment each plot Land parcels are 16m x 16m, or 52 square feet.",
            "symbols": [
                "ADDYY",
                "ETHUSD",
                "FB",
                "MANAUSD",
                "PONGF",
                "SANDUSD"
            ],
            "updated_at": "2022-06-09T18:08:20Z",
            "url": "https://www.benzinga.com/markets/cryptocurrency/22/06/27632130/virtual-land-just-sold-for-17-888-mana-in-decentraland"
        },
        {
            "author": "Benzinga Insights",
            "content": "",
            "created_at": "2022-06-09T18:08:12Z",
            "headline": "Virtual Land Just Sold For 2 ETH In The SandBox",
            "id": 27632128,
            "images": [
                {
                    "size": "large",
                    "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/images/story/2022/sandbox_nft_image_218.jpeg"
                },
                {
                    "size": "small",
                    "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/images/story/2022/sandbox_nft_image_218.jpeg"
                },
                {
                    "size": "thumb",
                    "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/images/story/2022/sandbox_nft_image_218.jpeg"
                }
            ],
            "source": "benzinga",
            "summary": "What happened: Virtual land tokenized as an NFT just sold for $4,057, which is 1.36x the current floor price of 1.655 Ether (CRYPTO: ETH). The estate consists of 166,464 plots of land –– each plot is 2,500 square feet in the metaverse.",
            "symbols": [
                "ADDYY",
                "ETHUSD",
                "FB",
                "MANAUSD",
                "PONGF",
                "SANDUSD"
            ],
            "updated_at": "2022-06-09T18:08:13Z",
            "url": "https://www.benzinga.com/markets/cryptocurrency/22/06/27632128/virtual-land-just-sold-for-2-eth-in-the-sandbox"
        },
        {
            "author": "Benzinga Insights",
            "content": "",
            "created_at": "2022-06-09T18:08:04Z",
            "headline": "Metaverse Land Just Sold For $4,328 In The SandBox",
            "id": 27632124,
            "images": [
                {
                    "size": "large",
                    "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/images/story/2022/sandbox_nft_image_217.jpeg"
                },
                {
                    "size": "small",
                    "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/images/story/2022/sandbox_nft_image_217.jpeg"
                },
                {
                    "size": "thumb",
                    "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/images/story/2022/sandbox_nft_image_217.jpeg"
                }
            ],
            "source": "benzinga",
            "summary": "What happened: Virtual land tokenized as an NFT just sold for $4,328, which is 1.45x the current floor price of 1.655 Ether (CRYPTO: ETH). The estate consists of 166,464 plots of land –– each plot is 2,500 square feet in the metaverse.",
            "symbols": [
                "ADDYY",
                "ETHUSD",
                "FB",
                "MANAUSD",
                "PONGF",
                "SANDUSD"
            ],
            "updated_at": "2022-06-09T18:08:05Z",
            "url": "https://www.benzinga.com/markets/cryptocurrency/22/06/27632124/metaverse-land-just-sold-for-4-328-2-eth-in-the-sandbox"
        },
        {
            "author": "Anusuya Lahiri",
            "content": "",
            "created_at": "2022-06-09T10:44:37Z",
            "headline": "Facebook Parent Meta Pauses Dual Camera Smartwatch Project",
            "id": 27622281,
            "images": [
                {
                    "size": "large",
                    "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/images/story/2022/06/09/abtech_0.png"
                },
                {
                    "size": "small",
                    "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/images/story/2022/06/09/abtech_0.png"
                },
                {
                    "size": "thumb",
                    "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/images/story/2022/06/09/abtech_0.png"
                }
            ],
            "source": "benzinga",
            "summary": "\n",
            "symbols": [
                "AAPL",
                "FB"
            ],
            "updated_at": "2022-06-09T10:44:38Z",
            "url": "https://www.benzinga.com/news/22/06/27622281/meta-pauses-dual-camera-smartwatch-project"
        },
        {
            "author": "Chris Katje",
            "content": "",
            "created_at": "2022-06-08T21:07:13Z",
            "headline": "Dustin Johnson Leads Inaugural LIV Golf Event: How To Watch, Betting Odds",
            "id": 27616521,
            "images": [
                {
                    "size": "large",
                    "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/images/story/2022/06/08/golf.mikael_damkier.shutterstock_158881226.jpg"
                },
                {
                    "size": "small",
                    "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/images/story/2022/06/08/golf.mikael_damkier.shutterstock_158881226.jpg"
                },
                {
                    "size": "thumb",
                    "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/images/story/2022/06/08/golf.mikael_damkier.shutterstock_158881226.jpg"
                }
            ],
            "source": "benzinga",
            "summary": "The inaugural LIV Golf Invitational Series kicks off Thursday, June 9. The league, funded by Saudi Arabia’s Public Investment Fund, is seeking to take on the PGA Tour with an alternative golf league.",
            "symbols": [
                "DKNG",
                "FB",
                "GOOG",
                "GOOGL"
            ],
            "updated_at": "2022-06-08T21:14:57Z",
            "url": "https://www.benzinga.com/news/22/06/27616521/dustin-johnson-leads-inaugural-liv-golf-event-how-to-watch-betting-odds"
        },
        {
            "author": "Benzinga Insights",
            "content": "",
            "created_at": "2022-06-08T19:02:08Z",
            "headline": "Metaverse Land Just Sold For $49,670 (50,000 MANA) In Decentraland",
            "id": 27614817,
            "images": [
                {
                    "size": "large",
                    "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/images/story/2022/decentraland_nft_image_175.png"
                },
                {
                    "size": "small",
                    "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/images/story/2022/decentraland_nft_image_175.png"
                },
                {
                    "size": "thumb",
                    "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/images/story/2022/decentraland_nft_image_175.png"
                }
            ],
            "source": "benzinga",
            "summary": "What happened: Virtual land tokenized as an NFT just sold for $49,670, which is 12.09x the current floor price of 2.286 Ethereum (CRYPTO: ETH) ($49,670 USD). The collection consists of over 97,000 plots of land –– at the current moment each plot Land parcels are 16m x 16m, or 52 square feet.",
            "symbols": [
                "ADDYY",
                "ETHUSD",
                "FB",
                "MANAUSD",
                "PONGF",
                "SANDUSD"
            ],
            "updated_at": "2022-06-08T19:02:09Z",
            "url": "https://www.benzinga.com/markets/cryptocurrency/22/06/27614817/metaverse-land-just-sold-for-49-670-50-000-mana-in-decentraland"
        },
        {
            "author": "Benzinga Insights",
            "content": "",
            "created_at": "2022-06-08T19:02:03Z",
            "headline": "This Plot Of Digital Land Just Sold For $78,479 In MANA In Decentraland",
            "id": 27614815,
            "images": [
                {
                    "size": "large",
                    "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/images/story/2022/decentraland_nft_image_174.png"
                },
                {
                    "size": "small",
                    "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/images/story/2022/decentraland_nft_image_174.png"
                },
                {
                    "size": "thumb",
                    "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/images/story/2022/decentraland_nft_image_174.png"
                }
            ],
            "source": "benzinga",
            "summary": "What happened: Virtual land tokenized as an NFT just sold for $78,479, which is 19.10x the current floor price of 2.286 Ethereum (CRYPTO: ETH) ($78,479 USD). The collection consists of over 97,000 plots of land –– at the current moment each plot Land parcels are 16m x 16m, or 52 square feet.",
            "symbols": [
                "ADDYY",
                "ETHUSD",
                "FB",
                "MANAUSD",
                "PONGF",
                "SANDUSD"
            ],
            "updated_at": "2022-06-08T19:02:04Z",
            "url": "https://www.benzinga.com/markets/cryptocurrency/22/06/27614815/this-plot-of-digital-land-just-sold-for-78-479-in-mana-in-decentraland"
        },
        {
            "author": "Benzinga Insights",
            "content": "",
            "created_at": "2022-06-08T19:01:47Z",
            "headline": "Virtual Land Just Sold For 2 ETH In The SandBox",
            "id": 27614812,
            "images": [
                {
                    "size": "large",
                    "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/images/story/2022/sandbox_nft_image_216.jpeg"
                },
                {
                    "size": "small",
                    "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/images/story/2022/sandbox_nft_image_216.jpeg"
                },
                {
                    "size": "thumb",
                    "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/images/story/2022/sandbox_nft_image_216.jpeg"
                }
            ],
            "source": "benzinga",
            "summary": "What happened: Virtual land tokenized as an NFT just sold for $3,603, which is 1.21x the current floor price of 1.65 Ether (CRYPTO: ETH). The estate consists of 166,464 plots of land –– each plot is 2,500 square feet in the metaverse.",
            "symbols": [
                "ADDYY",
                "ETHUSD",
                "FB",
                "MANAUSD",
                "PONGF",
                "SANDUSD"
            ],
            "updated_at": "2022-06-08T19:01:48Z",
            "url": "https://www.benzinga.com/markets/cryptocurrency/22/06/27614812/virtual-land-just-sold-for-2-eth-in-the-sandbox"
        },
        {
            "author": "Benzinga Insights",
            "content": "",
            "created_at": "2022-06-08T19:01:24Z",
            "headline": "Virtual Land Just Sold For 3 ETH In The SandBox",
            "id": 27614811,
            "images": [
                {
                    "size": "large",
                    "url": "https://cdn.benzinga.com/files/imagecache/2048x1536xUP/images/story/2022/sandbox_nft_image_215.jpeg"
                },
                {
                    "size": "small",
                    "url": "https://cdn.benzinga.com/files/imagecache/1024x768xUP/images/story/2022/sandbox_nft_image_215.jpeg"
                },
                {
                    "size": "thumb",
                    "url": "https://cdn.benzinga.com/files/imagecache/250x187xUP/images/story/2022/sandbox_nft_image_215.jpeg"
                }
            ],
            "source": "benzinga",
            "summary": "What happened: Virtual land tokenized as an NFT just sold for $4,774, which is 1.61x the current floor price of 1.65 Ether (CRYPTO: ETH). The estate consists of 166,464 plots of land –– each plot is 2,500 square feet in the metaverse.",
            "symbols": [
                "ADDYY",
                "ETHUSD",
                "FB",
                "MANAUSD",
                "PONGF",
                "SANDUSD"
            ],
            "updated_at": "2022-06-08T19:01:25Z",
            "url": "https://www.benzinga.com/markets/cryptocurrency/22/06/27614811/virtual-land-just-sold-for-3-eth-in-the-sandbox"
        },
        {
            "author": "Benzinga Newsdesk",
            "content": "",
            "created_at": "2022-06-08T17:28:18Z",
            "headline": "Top 15 Trending Stocks On WallStreetBets As Of Wednesday, June 8, 2022 (Via Swaggy Stocks)",
            "id": 27614164,
            "images": [],
            "source": "benzinga",
            "summary": "",
            "symbols": [
                "AAPL",
                "AMC",
                "AMD",
                "AMZN",
                "BABA",
                "FB",
                "GME",
                "INTC",
                "NIO",
                "ROKU",
                "TSLA",
                "WISH",
                "WMT",
                "XOM",
                "ZIM"
            ],
            "updated_at": "2022-06-08T17:28:19Z",
            "url": "https://www.benzinga.com/trading-ideas/22/06/27614164/top-15-trending-stocks-on-wallstreetbets-as-of-wednesday-june-8-2022-via-swaggy-stocks"
        }
    ]
    }
