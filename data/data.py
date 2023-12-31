valid_emails = [
    "example@example.com",
    "user12345@emaildomain.net",
    "john.doe@email-provider.org",
    "alice.smith1234@gmail.com",
    "test.user@email-tester.info",
    "sarah_jones@emailservice.org",
    "alexander123@myemaildomain.com",
    "emily.smith@emailplace.net",
    "robert.johnson@emailcenter.org",
    "anna.miller1234@emailbox.com",
    "maxwell.brown@emailhost.net",
    "linda_wilson@emailprovider.org",
    "david.clark@emailspot.com",
    "olivia.smith@emailplace.net",
    "andrew_lee@emailsite.info",
]

invalid_emails = [
    "",
    "example.com",
    "user12345@.net",
    "@email-provider.org",
    "alice.smith1234@gmail",
    "test.user@.info",
    "john.doe@com",
    "sarah_jones@.org",
    "alexander123@email.",
    "emily.smith@domain",
    "robert.johnson@12345",
    "anna.miller@com.",
    "maxwell.brown@host.",
    "linda_wilson@provider.",
    "david.clark@.com",
    "olivia.smith@place.",
]

valid_passwords = ["12345678", "qwertyui", "q1w2e3r4", "123456789"]

invalid_passwords = ["", "1234567", "qwertyu"]

invalid_ids = [
    1222222222222222222222222222222222222222222222222222222222222222,
    0,
    -10,
    "1235678",
]

invalid_space_id = [
    12222222222222222222222222222222222222222222222222222222222222222222222222222222222,
    0,
    -10,
]

invalid_project_limit = [
    -2,
    12222222222222222222222222222222222222222222222222222222222222222222222222222222222,
]

invalid_post_task_day_count = [
    -10,
    12222222222222222222222222222222222222222222222222222222222222222222222222222222222,
]

valid_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 111, 666]
invalid_orders = [
    12222222222222222222222222222222222222222222222222222222222222222222222222222222222
]
valid_orders = [
    12222222,
    0,
    -10,
]

boolean = [True, False]

invalid_names = ["", " "]
valid_names = ["1", "name"]
background_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

get_api = [
    "/admin/auth/refresh",
    "/admin/orders/1",
    "/admin/orders/1/invoice",
    "/admin/orders/1/oopd",
    "/admin/all-admins",
    "/admin/me",
    "/admin/organizations/1",
    "/admin/organizations/organization/1",
    "/admin/constants",
    "/user/me",
    "/user/organization",
    "/auth/refresh",
    "/notifications/firstUnread",
    "/notifications/1",
    "/notifications/archived/1",
    "/spaces",
    "/spaces/1/background",
    "/spaces/joinData/1",
    "/spaces/1/projects",
    "/spaces/1/reglaments",
    "/projects/all-projects",
    "/projects/1",
    "/projects/1/description",
    "/projects/1/tasks",
    "/projects/1/archiveTasks/1",
    "/projects/1/storageTasks/1",
    "/reglaments",
    "/reglaments/1",
    "/reglaments/1/questions",
    "/reglaments/1/history",
    "/tags",
    "/tasks",
    "/tasks/myHistory/1",
    "/tasks/1",
    "/tasks/1/description",
    "/tasks/1/history",
    "/tasks/1/messages",
    "/orders/1/invoice",
    "/orders/unpaid-license",
    "/files/avatar/123",
    "/files/project-files/1",
    "/constants",
    "/achievements",
]

post_api = [
    "/admin/auth/login",
    "/admin/orders/create",
    "/admin",
    "/admin/organizations/updateLicenseEnd/1",
    "/admin/organizations/updateUsersCount/1",
    "/admin/organizations/updateTrialEnd/1",
    "/admin/constants",
    "/user/avatar",
    "/auth/register",
    "/auth/login",
    "/auth/request-email-verification",
    "/auth/verify-email-registration",
    "/auth/verify-invite",
    "/auth/verify-email-change",
    "/auth/reset-password",
    "/auth/recover-password",
    "/reports/create-report",
    "/google/auth",
    "/mailru/auth",
    "/yandex/auth",
    "/yandex/get-tokens",
    "/spaces",
    "/spaces/join",
    "/spaces/1/share-link/off",
    "/spaces/1/share-link/on",
    "/spaces/1/columns",
    "/spaces/1/reglament-columns",
    "/spaces/1/share",
    "/projects",
    "/projects/1/stages",
    "/projects/1/embed",
    "/reglaments",
    "/reglaments/1/questions",
    "/reglaments/1/history",
    "/reglaments/1/complete-intro",
    "/reglaments/1/complete",
    "/reglaments/1/questions/1/answers",
    "/tags",
    "/tasks",
    "/tasks/duplicate",
    "/tasks/move",
    "/tasks/1/tag/1",
    "/tasks/1/add-member",
    "/tasks/1/messages",
    "/orders/payment-card",
    "/orders/payment-invoice",
    "/orders/1/cancel",
    "/payments/yookassaWebhook",
    "/files/initiateUpload",
    "/files/upload",
    "/files/completeUpload",
    "/files/delete-from-s3",
]
