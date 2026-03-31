from azureml.train.hyperdrive import HyperDriveConfig, PrimaryMetricGoal

hyperdrive_config = HyperDriveConfig(
    run_config=estimator,
    hyperparameter_sampling=param_sampling,
    primary_metric_name="accuracy",
    primary_metric_goal=PrimaryMetricGoal.MAXIMIZE,
    max_total_runs=20
)
