document.addEventListener('DOMContentLoaded', function () {
    // 为所有带有 .preview-btn 类的按钮绑定点击事件
    document.querySelectorAll('.preview-btn').forEach(function (button) {
        button.addEventListener('click', function () {
            const objectId = button.getAttribute('data-id');  // 获取对象 ID
            const modal = document.createElement('div');
            modal.classList.add('preview-modal');

            // 创建模态框的初始内容（加载中）
            modal.innerHTML = `
                <div class="preview-overlay"></div>
                <div class="preview-content">
                    <p>图片加载中...</p>
                    <button class="close-btn">关闭</button>
                </div>
            `;

            // 关闭模态框逻辑
            modal.querySelector('.close-btn').addEventListener('click', function () {
                document.body.removeChild(modal);
            });

            // 点击遮罩层关闭模态框
            modal.querySelector('.preview-overlay').addEventListener('click', function () {
                document.body.removeChild(modal);
            });

            // 将模态框添加到页面
            document.body.appendChild(modal);

            // 发送 AJAX 请求获取图片 URL
            fetch(`/industry_report_upload/get_image_url/${objectId}/`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('图片加载失败');
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.image_url) {
                        // 替换模态框内容为图片
                        modal.querySelector('.preview-content').innerHTML = `
                            <img src="${data.image_url}" alt="图片预览" />
                            <button class="close-btn">关闭</button>
                        `;
                        // 重新绑定关闭按钮
                        modal.querySelector('.close-btn').addEventListener('click', function () {
                            document.body.removeChild(modal);
                        });
                    } else {
                        modal.querySelector('.preview-content').innerHTML = `
                            <p>图片未找到</p>
                            <button class="close-btn">关闭</button>
                        `;
                    }
                })
                .catch(error => {
                    modal.querySelector('.preview-content').innerHTML = `
                        <p>加载失败，请重试</p>
                        <button class="close-btn">关闭</button>
                    `;
                });
        });
    });
});