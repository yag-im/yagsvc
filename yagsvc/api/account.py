from flask import (
    Blueprint,
    Response,
    request,
)
from flask_login import (
    current_user,
    login_required,
)

import yagsvc.biz.account as biz_account
from yagsvc.dto.account import (
    GetUserResponseDTO,
    UpdateUserRequestDTO,
)

bp = Blueprint("account", __name__, url_prefix="/api/accounts")


@bp.route("/user", methods=["GET"])
@login_required
def get_user() -> Response:
    """
    ---
    get:
        summary: Get user info.
        tags:
            - account
        responses:
            200:
                content:
                    application/json:
                        schema: GetUserResponseDTO
            401:
                description: Unauthorized user.
    """
    user_id = int(current_user.get_id())
    user = biz_account.get_user(user_id)
    return GetUserResponseDTO.Schema().dump(user)


@bp.route("/user", methods=["PUT"])
@login_required
def update_user() -> Response:
    """
    ---
    put:
        summary: Update user info.
        tags:
            - account
        requestBody:
            required: true
            content:
                application/json:
                    schema: UpdateUserRequestDTO
        responses:
            200:
                description: User info was successfully updated.
            401:
                description: Unauthorized user.
    """
    user_id = int(current_user.get_id())
    user = UpdateUserRequestDTO.Schema().load(data=request.get_json())
    biz_account.update_user(user_id, user)
    return "", 200
